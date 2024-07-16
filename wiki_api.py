import requests
import time
import random

def fetch_wikipedia_data(name, sport):
    # Use Wikipedia API to search for the athlete
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={name}%20{sport}&format=json"
    response = requests.get(search_url)
    if response.status_code == 200:
        search_results = response.json().get('query', {}).get('search', [])
        if search_results:
            # Fetch the page content of the first search result
            page_id = search_results[0]['pageid']
            page_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids={page_id}&format=json"
            page_response = requests.get(page_url)
            if page_response.status_code == 200:
                page_data = page_response.json().get('query', {}).get('pages', {}).get(str(page_id), {})
                extract = page_data.get('extract', '')
                return extract
    return None

# Example usage
athlete_name = "Danielle Collins"
athlete_sport = "Tennis"
data = fetch_wikipedia_data(athlete_name, athlete_sport)
print(data)

# Add a delay to avoid making too many requests in a short period
time.sleep(random.uniform(1, 3))