import pandas as pd

# CSV Files Load
results_df = pd.read_csv('evo_results.csv')
characters_df = pd.read_csv('top_street_fighter_character.csv')

# Convert Year column to strings due to Nan error
results_df['Year'] = results_df['Year'].astype(str)
characters_df['Year'] = characters_df['Year'].astype(str)


merged_df = pd.merge(results_df, characters_df, on='Year', how='left')


merged_df.to_csv('character_master_file.csv', index=False)


print(merged_df)