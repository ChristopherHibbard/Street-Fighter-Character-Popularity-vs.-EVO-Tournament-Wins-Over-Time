#Web Scraper#
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the EVO results page
url = "https://streetfighter.fandom.com/wiki/Evolution_Championship_Series#Results"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all tables with the 'wikitable' class
tables = soup.find_all('table', {'class': 'wikitable'})

# List to hold all DataFrames
all_tables = []

# Loop through each table
for table_index, table in enumerate(tables, start=1):
    rows = table.find_all('tr')
    data = []

    # Extract the closest header for the table
    table_header = table.find_previous(['h2', 'h3'])  # Look for the nearest <h2> or <h3>
    if table_header:
        table_id = table_header.text.strip()
    else:
        table_id = f"Table_{table_index}"  # Fallback if no header is found

    # Attempt to extract year from the table header
    year = ''.join(filter(str.isdigit, table_id))[:4] if any(char.isdigit() for char in table_id) else "Unknown"

    # Process each row in the table
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        # Standardize row length by padding with None
        while len(cols) < 5:
            cols.append(None)

        if cols:
            data.append(cols)

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=['Column_1', 'Column_2', 'Column_3', 'Column_4', 'Column_5'])

    # Rename columns
    df.rename(
        columns={
            'Column_1': 'Place',
            'Column_2': 'Player',
            'Column_3': 'Player Alias',
            'Column_4': 'Street Fighter Character(s) Used',
            'Column_5': 'Additional Info'
        },
        inplace=True
    )

    # Add Table_ID and Year columns
    df['Table_ID'] = table_id
    df['Year'] = year

    # Append the DataFrame to the list
    all_tables.append(df)

# Combine all DataFrames into a single DataFrame
combined_df = pd.concat(all_tables, ignore_index=True)

# Save the combined data to a CSV file
combined_df.to_csv('evo_results_all_tables_fixed.csv', index=False)

# Display the first few rows to check the combined data
print(combined_df.head())