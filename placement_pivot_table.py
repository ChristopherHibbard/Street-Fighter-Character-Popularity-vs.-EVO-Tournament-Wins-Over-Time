import pandas as pd

# Read the CSV data into a DataFrame
df = pd.read_csv('character_master_file.csv')

# Filter rows where the Top Character matches the Character(s)
df_filtered = df[df['Top Character'] == df['Character(s)']]

# Create a pivot table: The index is the 'Year' and 'Character(s)', 
# the columns are 'Place' (1st, 2nd, 3rd, etc.), and the values are 'Top Character' 
# with aggregation as count (we'll just count instances of players)
pivot_table = df_filtered.pivot_table(
    values='Player',  # Or you could use 'Alias' to count
    index=['Year', 'Character(s)'],  # Index by Year and Character(s)
    columns='Place',  # Columns for placement (1st, 2nd, 3rd, etc.)
    aggfunc='count',  # We are counting the number of players per placement
    fill_value=0      # Fill missing placements with 0
)

# Print the pivot table
print(pivot_table)

# Save the pivot table to a CSV file
pivot_table.to_csv('filtered_pivot_table.csv')

# Optional: Inform user that the CSV has been saved
print("Pivot table saved to 'filtered_pivot_table.csv'")