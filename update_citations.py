import os, requests, json

API_KEY = os.getenv("SERPAPI_KEY")
SCHOLAR_ID = "czJoNWIAAAAJ" 
def get_citations(): 
    url = f"https://serpapi.com/search.json?engine=google_scholar_author&author_id={SCHOLAR_ID}&api_key={API_KEY}" 
    r = requests.get(url) 
    data = r.json() 
    table = data.get("cited_by", {}).get("table", [{}])
    return table[0].get("citations", {}).get("all", 0), table[1].get("h_index", {}).get("all", 0) 

def main(): 
    citations, h_index = get_citations() 
    with open("citations.json", "w") as f: 
        json.dump({"citations": citations}, f) 
    with open("h_index.json", "w") as f: 
        json.dump({"h_index": h_index}, f) 

if __name__ == "__main__": 
    main()
