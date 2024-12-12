import pandas as pd

# CSV to df
df = pd.read_csv('CSVs Files/character_master_file.csv')

# Filter: Matching Top Character to Character(s)
df_filtered = df[df['Top Character'] == df['Character(s)']]

# Pivot table creation. Index is Year and Character(s), 
# Columns are place (placment) 
# Aggregation is count

pivot_table = df_filtered.pivot_table(
    values='Player',  
    index=['Year', 'Character(s)'],  
    columns='Place',  
    aggfunc='count',  
    fill_value=0      
)


print(pivot_table)


pivot_table.to_csv('CSVs Files/filtered_pivot_table.csv')


print("Pivot table saved to 'filtered_pivot_table.csv'")