from bs4 import BeautifulSoup
import re
import requests

def fetch_infobox_html(name):
    # Replace spaces in the name with underscores for the API request
    formatted_name = name.replace(' ', '_')
    # Wikipedia API request URL with rvparse parameter
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles={formatted_name}&rvsection=0&rvparse"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Extract HTML content from API response
            page_one = next(iter(data['query']['pages'].values()))
            revisions = page_one.get('revisions', [])
            html_content = next(iter(revisions[0].values()))
            return html_content
        else:
            print(f"Error fetching Wikipedia data: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request error: {e}")
    
    return None

def extract_college_from_infobox(html):
    # Parse HTML using BeautifulSoup to extract infobox
    soup = BeautifulSoup(html, 'html.parser')
    infobox = soup.find('table', class_='infobox')
    if infobox:
        # Define keywords to look for in the infobox data
        keywords = ['college', 'college team', 'university']
        
        # Search for relevant keywords in infobox rows
        for keyword in keywords:
            pattern = re.compile(rf'\b{keyword}\b', flags=re.IGNORECASE)
            row = infobox.find('th', text=pattern)
            if row:
                college_name = row.find_next_sibling('td')
                if college_name:
                    return college_name.text.strip()
        
        return "College/University information not found."
    else:
        return "No Infobox found."

# Test Case
def test_fetch_and_parse_infobox():
    athlete_name = "Siobhán Haughey"
    html_content = fetch_infobox_html(athlete_name)
    if html_content:
        print(f"Infobox HTML content for {athlete_name}:")
        print(extract_college_from_infobox(html_content))
    else:
        print(f"Failed to fetch Wikipedia data for {athlete_name}")

# Execute the test case
test_fetch_and_parse_infobox()