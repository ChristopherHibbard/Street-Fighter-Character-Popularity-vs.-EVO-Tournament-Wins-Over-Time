import pandas as pd

# Load the event results CSV
results_df = pd.read_csv('evo_results.csv')

# Load the top character CSV
characters_df = pd.read_csv('Top_Street_Fighter_Character.csv')

# Merge the datasets on the 'Year' column
merged_df = pd.merge(results_df, characters_df, on='Year', how='left')

# Save the merged dataframe to a new CSV file
merged_df.to_csv('Character_Master_File.csv', index=False)

# Display the first few rows of the merged dataframe
print(merged_df.head())