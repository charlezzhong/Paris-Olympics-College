import pandas as pd
import requests
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the API key
API_KEY = os.getenv('API_KEY')
CSE_ID = os.getenv('CSE_ID')


def google_search(query, api_key, cse_id, num_results=10):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}&num={num_results}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def extract_university(search_results):
    # Placeholder function to extract university from search results
    for item in search_results.get('items', []):
        title = item.get('title')
        snippet = item.get('snippet')
        if 'University' in title or 'University' in snippet:
            return item['title']
    return 'Unknown University'
    
query = f'"charlie swanson" "swimming" "university"'
search_results = google_search(query, API_KEY, CSE_ID)
found_university = extract_university(search_results)
print(found_university)

"""def extract_university(search_results):
    # Placeholder function to extract university from search results
    for item in search_results.get('items', []):
        title = item.get('title')
        snippet = item.get('snippet')
        if 'University' in title or 'University' in snippet:
            return item['title']
    return 'Unknown University'

# Read CSV file
athletes = pd.read_csv('athletes.csv')

# Prepare results dictionary
results = []

for index, row in athletes.iterrows():
    name = row['name']
    sport = row['sport']
    
    query = f'"{name}" "{sport}" "university"'
    search_results = google_search(query, API_KEY, CSE_ID)
    
    if search_results:
        found_university = extract_university(search_results)
        results.append({'name': name, 'sport': sport, 'university': found_university})
    else:
        results.append({'name': name, 'sport': sport, 'university': 'Search Failed'})

# Convert results to DataFrame and save to CSV
results_df = pd.DataFrame(results)
results_df.to_csv('athletes_universities.csv', index=False)"""