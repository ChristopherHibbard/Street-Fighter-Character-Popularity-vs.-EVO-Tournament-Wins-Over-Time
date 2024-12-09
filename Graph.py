import pandas as pd
import matplotlib.pyplot as plt

# Read pivot table CSV
pivot_table = pd.read_csv('filtered_pivot_table.csv', index_col=['Year', 'Character(s)'])

# Index reset for easier reading without errors
pivot_table_reset = pivot_table.reset_index()

# Numeric conversvion
placement_columns = pivot_table_reset.columns.difference(['Year', 'Character(s)'])
pivot_table_reset[placement_columns] = pivot_table_reset[placement_columns].apply(pd.to_numeric, errors='coerce', axis=1)

# Calculating sum of placements and group together in a year
yearly_sums = pivot_table_reset.groupby('Year')[placement_columns].sum().sum(axis=1)

# Index of years creation
full_year_range = pd.RangeIndex(start=yearly_sums.index.min(), stop=yearly_sums.index.max() + 1)

# Include every year range from 2002-present
yearly_sums = yearly_sums.reindex(full_year_range, fill_value=0)

# Prepare the plot
plt.figure(figsize=(12, 6))

# Create bar graph
plt.bar(yearly_sums.index, yearly_sums.values, color='skyblue', edgecolor='black')

# Customization of Graph
plt.title('Street Fighter EVO Tournament Popular Character Placement Per Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Total Placements (1st-7th)', fontsize=14)
plt.xticks(yearly_sums.index, rotation=45)
plt.tight_layout()

# Save and show
plt.savefig('Popular_character_placement.png')  
plt.show()  
