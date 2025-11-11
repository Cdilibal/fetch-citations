import json
from scholarly import scholarly

USER_ID = "czJoNWIAAAAJ"

def get_citations():
    author = scholarly.search_author_id(USER_ID)
    author = scholarly.fill(author, sections=['indices'])
    return author.get("citedby", 0)

def main():
    count = get_citations()
    data = {"citations": count}
    with open("citations.json", "w") as f:
        json.dump(data, f)
    print(f"Updated citations: {count}")

if __name__ == "__main__":
    main()
