import requests, json, os

API_KEY = os.getenv("SERPAPI_KEY")
SCHOLAR_ID = "ABC123"

def get_citations():
    url = f"https://serpapi.com/search.json?engine=google_scholar_author&author_id={SCHOLAR_ID}&api_key={API_KEY}"
    r = requests.get(url)
    data = r.json()
    return data.get("cited_by", {}).get("table", [{}])[0].get("citations", {}).get("all", 0)

def main():
    count = get_citations()
    with open("citations.json", "w") as f:
        json.dump({"citations": count}, f)
    print(f"Updated citations: {count}")

if __name__ == "__main__":
    main()
