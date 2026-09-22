from utilities import fetch_publications, add_missing_publications
import sys

def main(path="content/publications/"):
    # Replace accordingly
    scholar_url = "https://scholar.google.com/citations?user=8aN-HtMAAAAJ&hl=en"
    # Author name (for proper highlighting) Replace accordingly
    author_name = "João Lourenço"

    # Read publication from Google Scholar
    publications = fetch_publications(scholar_url, verbose = True)

    add_missing_publications(publications, path, author_name, verbose = True)

if __name__ == "__main__":
    """Allow the path to be passed as an argument when the script is executed directly"""
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "content/publications/"
    main(path)
