from scholarly import scholarly, ProxyGenerator
from utilities import fetch_publications, add_missing_publications
import sys

def main(path="content/publications/"):
    # Replace accordingly
    scholar_url = "https://scholar.google.com/citations?user=8aN-HtMAAAAJ&hl=en"
    # Author name (for proper highlighting) Replace accordingly
    author_name = "João Lourenço"

    # Route requests through rotating free proxies to avoid Google's IP-based
    # blocking of repeated direct requests.
    print("Setting up proxy rotation...", flush=True)
    pg = ProxyGenerator()
    success = pg.FreeProxies()
    print(f"Proxy setup {'succeeded' if success else 'failed, falling back to direct requests'}", flush=True)
    if success:
        scholarly.use_proxy(pg)

    # Read publications from Google Scholar (with a delay between each
    # publication's detail fetch to avoid tripping rate limits). Each one is
    # written to disk as soon as it's fetched, so a crash or a single bad
    # item partway through doesn't lose everything already collected.
    publications = fetch_publications(
        scholar_url, verbose=True, delay_seconds=6,
        author_name=author_name, save_path=path,
    )

    # Safety net: catch anything that wasn't saved inline (a no-op for
    # already-saved entries, since save_to_file skips existing folders).
    add_missing_publications(publications, path, author_name, verbose = True)

if __name__ == "__main__":
    """Allow the path to be passed as an argument when the script is executed directly"""
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "content/publications/"
    main(path)
