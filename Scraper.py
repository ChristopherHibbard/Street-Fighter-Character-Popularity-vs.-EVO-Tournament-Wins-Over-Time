#Web Scraper#
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the EVO results page
url = "https://streetfighter.fandom.com/wiki/Evolution_Championship_Series#Results"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize a list to store all the tournament data
all_data = []

# Find all tables on the page (for each game and event)
tables = soup.find_all('table', {'class': 'wikitable'})

# Loop through each table
for table in tables:
    # Extract the event name from the <h3> tag above the table
    event_header = table.find_previous('h3')
    event_name = event_header.text.strip() if event_header else 'Unknown Event'

    # Extract the year from the <p> tag after the event title
    year = None
    p_tag = table.find_previous('p')
    if p_tag:
        year_text = p_tag.text.strip()
        # Attempt to extract the year from the text (the year should typically be 4 digits)
        for word in year_text.split():
            if word.isdigit() and len(word) == 4:
                year = word
                break

    if not year:
        year = 'Unknown Year'

    # Extract rows of the table and loop through them (skip the header row)
    rows = table.find_all('tr')[1:]  # Skip the header row
    
    for row in rows:
        cols = row.find_all('td')
        
        if len(cols) < 4:  # Skip rows that do not have enough columns
            continue

        place = cols[0].text.strip()
        player = cols[1].text.strip()
        alias = cols[2].text.strip()
        characters = cols[3].text.strip()

        # Skip if there are multiple players listed (i.e., team matches)
        if ',' in player or 'and' in player:
            continue

        # Store data as a row in a list
        all_data.append([place, player, alias, characters, event_name, year])

# Convert the list of data into a DataFrame
df = pd.DataFrame(all_data, columns=['Place', 'Player', 'Alias', 'Character(s)', 'Event Name', 'Year'])

# Save the DataFrame to a CSV file
df.to_csv('evo_results.csv', index=False)

# Display the DataFrame for verification
print(df.head())