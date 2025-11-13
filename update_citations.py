import requests
import json
import os

API_KEY = os.getenv("SERPAPI_KEY")
SCHOLAR_ID = "czJoNWIAAAAJ"

def get_citations():
    url = f"https://serpapi.com/search.json?engine=google_scholar_author&author_id={SCHOLAR_ID}&api_key={API_KEY}"
    r = requests.get(url)
    data = r.json()

    cited_by = data.get("cited_by", {})
    table = cited_by.get("table", [])

    if not table:
        print("Warning: 'cited_by.table' missing or empty. Raw keys:", list(cited_by.keys()))
        return 0, 0

    first = table[0]
    citations = first.get("citations", {}).get("all", 0)
    h_index = first.get("h_index", {}).get("all", 0)

    if not h_index and "h_index" in cited_by:
        h_index = cited_by.get("h_index", {}).get("all", 0)

    return citations, h_index


def main():
    citations, h_index = get_citations()

    with open("citations.json", "w") as f:
        json.dump({"citations": citations}, f, indent=2)

    with open("h_index.json", "w") as f:
        json.dump({"h_index": h_index}, f, indent=2)

    print(f"Updated citations: {citations}, h-index: {h_index}")


if __name__ == "__main__":
    main()
