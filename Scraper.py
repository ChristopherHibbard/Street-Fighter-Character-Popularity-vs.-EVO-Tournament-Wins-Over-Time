#Web scraper#
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the EVO results page (replace with actual URL)
url = "https://streetfighter.fandom.com/wiki/Evolution_Championship_Series#Results"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract tournament table data
table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')

# Process each row
data = []
for row in rows[1:]:  # Skip header
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    
    # Ensure the row has exactly 5 elements, filling missing values with None
    while len(cols) < 5:
        cols.append(None)
    
    if cols:
        data.append(cols)

# Save to DataFrame
df = pd.DataFrame(data, columns=['Place', 'Player', 'Character', 'Date', 'Game'])

# Display the first few rows to check the data
print(df.head())

# Save to CSV
df.to_csv('evo_results_2023.csv', index=False)