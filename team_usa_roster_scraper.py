import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = "https://www.nbclosangeles.com/paris-2024-summer-olympics/team-usa-full-roster-2024-olympics/3450706"

# Send a GET request to the website
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Open a CSV file to write the data
with open('team_usa_roster_2024_olympics.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Name', 'Sport', 'Gender/Category'])

    # Find all <h2> tags with the class "wp-block-nbc-section-heading"
    sections = soup.find_all('h2', class_='wp-block-nbc-section-heading')

    # Iterate over each section (sport)
    for section in sections:
        sport = section.text
        # Get the next sibling elements until the next <h2> tag
        sibling = section.find_next_sibling()
        while sibling and sibling.name != 'h2':
            if sibling.name == 'p' and sibling.strong:
                gender = sibling.strong.text
            elif sibling.name == 'ul':
                athletes = sibling.find_all('li')
                for athlete in athletes:
                    name = athlete.text
                    writer.writerow([name, sport, gender])
            sibling = sibling.find_next_sibling()
