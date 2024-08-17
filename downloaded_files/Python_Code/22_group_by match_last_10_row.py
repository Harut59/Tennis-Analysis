# import pandas as pd
#
# # Sample DataFrame
#
#
# df = pd.read_csv('all_sport_gen_site.csv')
# df = df[df['Total'] != 0]
# df = df[df['modified_fora'] != 0]
# # Group by 'standardized_match' and take the last 10 rows of each group
#
# last_10_per_group = df.groupby('standardized_match', group_keys=False).apply(lambda x: x.head(10)).reset_index(drop=True)
#
# # Calculate the average 'total' for each 'standardized_match' group from the last 10 rows
# average_total = last_10_per_group.groupby('standardized_match')['Total'].mean().reset_index()
# average_fora = last_10_per_group.groupby('standardized_match')['modified_fora'].mean().reset_index()
# print(average_total,average_fora)
#
# # Rename the average column to 'average_total'
# # average_total.rename(columns={'total': 'average_total'}, inplace=True)
# average_total.to_csv('all_sport_gen_site_group_by_last_10_row.csv', index=False)
# average_fora.to_csv('all_sport_gen_site_group_by_last_10_row.csv', index=False)

import pandas as pd

# Load the data
df = pd.read_csv('../../all_sport_gen_site.csv')
df = df[df['Total'] != 0]
df = df[df['modified_fora'] != 0]

# Group by 'standardized_match' and take the last 10 rows of each group
last_10_per_group = df.groupby('standardized_match', group_keys=False).apply(lambda x: x.head(10)).reset_index(drop=True)

# Calculate the average 'Total' and 'modified_fora' for each 'standardized_match' group from the last 10 rows
average_total = last_10_per_group.groupby('standardized_match')['Total'].mean().reset_index()
average_fora = last_10_per_group.groupby('standardized_match')['modified_fora'].mean().reset_index()

# Merge the two DataFrames on 'standardized_match'
average_combined = pd.merge(average_total, average_fora, on='standardized_match', suffixes=('_total', '_fora'))

# Rename columns for clarity
#average_combined.rename(columns={'Total_total': 'average_total', 'modified_fora_fora': 'average_fora'}, inplace=True)

# Save the result to a CSV file
average_combined.to_csv('all_sport_gen_site_group_by_last_10_row.csv', index=False)
