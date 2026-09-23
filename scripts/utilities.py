from scholarly import scholarly
import os
import re
import time
import difflib
import requests

def is_valid_doi(doi):
    # Regex to match standard DOI pattern (e.g., 10.xxxx/xxxxxxx)
    doi_pattern = r"^10\.\d{4,9}/[-._;()/:A-Z0-9]+$"
    # Test if the DOI matches the pattern
    return bool(re.match(doi_pattern, doi))

def _normalize_title(title):
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()

def enrich_with_crossref(publication, min_similarity=0.85, verbose=True):
    """Cross-check a publication against Crossref (by title) to fill in
    fields Google Scholar left blank/unknown: journal, volume, issue, doi.
    Never overwrites a field that already has a real value - only fills gaps,
    and only when the returned title is a close match to ours, to avoid
    attaching the wrong record.
    """
    title = publication.get('title', '')
    if not title or title == 'N/A':
        return publication

    try:
        resp = requests.get(
            "https://api.crossref.org/works",
            params={"query.bibliographic": title, "rows": 3},
            timeout=15,
        )
        resp.raise_for_status()
        items = resp.json().get('message', {}).get('items', [])
    except Exception as e:
        if verbose:
            print(f"\033[33mCrossref lookup failed for '{title[:40]}...': {e}\033[0m", flush=True)
        return publication

    our_norm = _normalize_title(title)
    best = None
    best_ratio = 0.0
    for item in items:
        candidate_titles = item.get('title') or []
        if not candidate_titles:
            continue
        # Crossref often splits "Title: Subtitle" into separate `title` and
        # `subtitle` fields, so compare against both the bare title and the
        # title+subtitle joined, and keep whichever scores higher.
        candidates = [candidate_titles[0]]
        subtitles = item.get('subtitle') or []
        if subtitles:
            candidates.append(f"{candidate_titles[0]}: {subtitles[0]}")
        ratio = max(
            difflib.SequenceMatcher(None, our_norm, _normalize_title(c)).ratio()
            for c in candidates
        )
        if ratio > best_ratio:
            best_ratio = ratio
            best = item

    if best is None or best_ratio < min_similarity:
        return publication

    filled = []

    journal = publication.get('journal', 'N/A')
    if journal in ('N/A', 'Unknown Journal', '') and best.get('container-title'):
        publication['journal'] = best['container-title'][0]
        filled.append('journal')

    volume = publication.get('volume', 'N/A')
    if volume in ('N/A', '') and best.get('volume'):
        publication['volume'] = best['volume']
        filled.append('volume')

    issue = publication.get('issue', 'N/A')
    if issue in ('N/A', '') and best.get('issue'):
        publication['issue'] = best['issue']
        filled.append('issue')

    doi = publication.get('doi', 'N/A')
    if doi in ('N/A', '') and best.get('DOI'):
        publication['doi'] = best['DOI']
        if publication.get('url', 'N/A') in ('N/A', ''):
            publication['url'] = f"https://doi.org/{best['DOI']}"
        filled.append('doi')

    if verbose and filled:
        print(f"\033[32mCrossref filled {', '.join(filled)} (match {best_ratio:.2f})\033[0m", flush=True)

    return publication

def fetch_publications(profile_url, verbose = True, delay_seconds = 0, author_name = None, save_path = None):
    """Fetch all publications from a Google Scholar profile.

    If `save_path` is given, each publication is written to disk immediately
    after it's successfully fetched (via `save_to_file`), so a crash or a
    single bad item midway through a long run doesn't lose everything
    already collected.
    """
    # Extract the user ID from the URL
    user_id = profile_url.split("user=")[1].split("&")[0]
    print(f"Looking up author id {user_id}...", flush=True)
    author = scholarly.search_author_id(user_id)
    scholar_author_name = author['name']

    if verbose:
        print("\033[35mFetching publications for:\033[0m", flush=True)
        print(f"\033[35mUser ID = {user_id}\033[0m", flush=True)
        print(f"\033[35mUser name = {scholar_author_name}\033[0m", flush=True)

    if author_name is None:
        author_name = scholar_author_name

    # Search for the profile
    search_query = scholarly.search_author_id(user_id)
    profile = scholarly.fill(search_query)

    # Collect publications
    all_pubs = profile.get('publications', [])
    print(f"Found {len(all_pubs)} publication stubs, fetching details...", flush=True)
    publications = []
    for i, pub in enumerate(all_pubs):
        print(f"[{i+1}/{len(all_pubs)}] fetching details...", flush=True)
        try:
            pub_details = scholarly.fill(pub)
            if delay_seconds:
                time.sleep(delay_seconds)
            title = pub_details.get('bib', {}).get('title', 'N/A')
            journal = pub_details.get('bib', {}).get('journal', 'N/A')
            author = pub_details.get('bib', {}).get('author', 'N/A')
            abstract = pub_details.get('bib', {}).get('abstract', 'N/A')
            volume = pub_details.get('bib', {}).get('volume', 'N/A')
            issue = pub_details.get('bib', {}).get('number', 'N/A'),
            if isinstance(issue, tuple):  # Check if 'issue' is a tuple
                issue = issue[0] # Extract the first element from the tuple

            # Try to get the doi
            full_doi = pub_details.get('doi', 'N/A')
            if full_doi == 'N/A':
                full_doi = pub_details.get('bib', {}).get('doi', 'N/A')
            if full_doi == 'N/A':
                full_doi = pub_details.get('url', 'N/A')
            if full_doi == 'N/A':
                full_doi = pub_details.get('eprint_url', 'N/A')
            if full_doi == 'N/A':
                full_doi = pub_details.get('pub_url', 'N/A')

            # Try to get the primary URL
            url = pub_details.get('url', 'N/A')
            if url == 'N/A':
                url = pub_details.get('eprint_url', 'N/A')
            if url == 'N/A':
                url = pub_details.get('pub_url', 'N/A')
            if (url == 'N/A') & (full_doi != 'N/A'):
                url = full_doi  # Use DOI as a fallback URL
            if full_doi == 'N/A' and url != 'N/A':
                full_doi = url

            if (full_doi != 'N/A'):
                if is_valid_doi(full_doi.split('/')[-2]+"/"+full_doi.split('/')[-1]):
                    full_doi = full_doi.split('/')[-2]+"/"+full_doi.split('/')[-1]

            # Try date-related information
            year = pub_details.get('bib', {}).get('pub_year', 'N/A')
            month = pub_details.get('bib', {}).get('pub_month', 'N/A')
            day = pub_details.get('bib', {}).get('pub_day', 'N/A')
            # Define date
            if year != 'N/A':
                if month != 'N/A' and day != 'N/A':
                    # If month and day are available, use them
                    date_value = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                elif month != 'N/A':
                    # If only month is available, assume the first day
                    date_value = f"{year}-{month.zfill(2)}-01"
                else:
                    # If only year is available, assume January 1st
                    date_value = f"{year}-01-01"
            else:
                # If no year is available, set date as N/A
                date_value = 'N/A'

            is_preprint = "arXiv" in pub_details.get('bib', {}).get('journal', '') or "bioRxiv" in pub_details.get('bib', {}).get('journal', '')
            if isinstance(is_preprint, tuple):  # Check if 'issue' is a tuple
                is_preprint = is_preprint[0] # Extract the first element from the tuple

            journal, _ = manage_exception(journal, title, "")

            if "Unknown Journal" in journal:
                if "hal.science" in url:
                    journal = "HAL"

            # Debugging missing years
            if year == 'N/A':
                print(f"Missing year for publication: {pub_details.get('bib', {}).get('title', 'Unknown Title')}")

            publication_data = {
                'title': title,
                'author': author,
                'journal': journal,
                'year': year,
                'url': url,
                'abstract': abstract,
                'doi': full_doi,
                'volume': volume,
                'issue': issue,
                'is_preprint': is_preprint,
                'date': date_value,
            }

            publication_data = enrich_with_crossref(publication_data, verbose=verbose)

            if verbose:
                truncated_title = title if len(title) <= 30 else title[:27] + "..."
                print(f"\033[36m{year}\033[0m {truncated_title} \033[36m{publication_data['journal']}\033[0m")

            publications.append(publication_data)

            if save_path is not None:
                folder_name = define_folder_name(publication_data)
                save_to_file(publication_data, save_path, folder_name, author_name, verbose)

        except Exception as e:
            print(f"\033[31mSkipping publication {i+1}/{len(all_pubs)} due to error: {e}\033[0m", flush=True)
            continue

    if verbose:
        print("\n")
        print(f"\033[35m{len(publications)} publications found\033[0m")
        print("\n")

    # Sort the publications
    publications.sort(
        key=lambda x: int(x.get('year')) if str(x.get('year')).isdigit() else 0,
        reverse=False
    )

    return publications

def manage_exception(journal, title, family_name):
    # Manage exceptions, such as non-journal articles, theses, etc.
    # Adapt to your own case as needed.
    if "arXiv" in journal:
        journal = "arXiv"
    elif journal.lower() in ["n/a", "unknown", ""]:
        journal = "Unknown Journal"
    return journal, family_name

def define_folder_name(publication):
    """Read publication information and define folder name from it"""
    title = publication["title"]
    year = publication.get('year', 'Unknown')
    volume = publication.get('volume', 'Unknown')
    issue = publication.get('issue', 'Unknown')

    # Extract the first author's last name
    authors = publication.get('author', 'unknown')
    if authors.lower() == "unknown" or not authors.strip():
        family_name = "Unknown_Author"
    else:
        first_author = authors.split(' and ')[0].strip() if ' and ' in authors else authors.split(',')[0].strip()
        family_name = first_author.split()[-1] if first_author else "Unknown_Author"
        journal = publication.get('journal', 'Unknown_Journal').replace(' ', '_')

    journal, family_name = manage_exception(journal, title, family_name)

    if ("N/A" not in volume) & ("N/A" not in issue):
        folder_name = str(year)+"_"+volume+"_"+issue+"_"+family_name+"_"+journal
    elif ("N/A" not in volume):
        folder_name = str(year)+"_"+volume+"_"+family_name+"_"+journal
    else:
        folder_name = str(year)+"_"+family_name+"_"+journal

    folder_name = folder_name + "_" + "_".join(title.split(" ")[:3])

    return folder_name

def add_missing_publications(publications, path_to_publications, author_name, verbose = True):
    """Loop over publications, and check if they are already present in path_to_publications."""
    for publication in publications:
        folder_name = define_folder_name(publication)
        if folder_name is not None:
            save_to_file(publication, path_to_publications, folder_name, author_name, verbose)

def save_to_file(pub, path, folder, author_name, verbose):
    """Save publication to an individual Markdown-like file."""
    if not os.path.exists(path):
        os.makedirs(path)

    # Determine publication type
    is_preprint = pub.get('is_preprint', False)
    if is_preprint:
        publication_type = "3"
    else:
        publication_type = "2"

    date = pub.get('date', 'N/A') or 'N/A'
    title = pub.get('title', 'N/A')
    authors = pub.get('author', 'N/A')
    journal = pub.get('journal', 'N/A')
    url = pub.get('url', 'N/A')
    abstract = pub.get('abstract', 'N/A')
    year = pub.get('year', None)
    volume = pub.get('volume', None)
    issue = pub.get('issue', None)

    # Split authors string into a list if needed
    if isinstance(authors, str):
        authors = [author.strip() for author in authors.split(" and ")]

    # Apply **formatting** to highlight the site owner's name
    formatted_authors = [
        f"**{author}**" if author == author_name else author for author in authors
    ]
    authors_str = ", ".join(f'"{author}"' for author in formatted_authors)

    # Construct publication string
    publication_entry = f"{journal} "
    if year:
        publication_entry += f"{year} "
    if volume:
        if 'N/A' not in volume:
            publication_entry += f"{volume} "
    if issue:
        if 'N/A' not in issue:
            publication_entry += f"({issue})"

    content = f"""---
title: "{title}"
date: {date}
publishDate: {date}
authors: {"["+authors_str+"]"}
publication_types: ["{publication_type}"]
abstract: "{abstract.replace(chr(10), ' ').replace(chr(34), chr(39))}"
featured: true
publication: "{publication_entry}"
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: '{url}'
---
"""

    if not os.path.exists(path + folder):
        os.makedirs(path + folder)
        with open(path + folder + "/index.md", mode='w', encoding='utf-8') as file:
            file.write(content)
        if verbose:
            print(f"\033[96m{folder} created\033[0m")
    else:
        if verbose:
            print(f"\033[34m{folder} already exists\033[0m")
