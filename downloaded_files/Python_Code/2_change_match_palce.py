import pandas as pd

# Load the CSV file
df = pd.read_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\2024-07-01.csv')

# Function to standardize match pairs
def standardize_match(row):
    player1 = row['player_1']
    player2 = row['player_2']
    if player1 < player2:
        return f"{player1} - {player2}"
    else:
        return f"{player2} - {player1}"

# Apply the function to create a new column
df['standardized_match'] = df.apply(standardize_match, axis=1)

# Save the DataFrame back to a CSV file
#df.to_csv('matches_with_standardized_1.csv', index=False)
df.to_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\2024-07-01.csv', index=False)
#df.to_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\2024-06-30.csv', index=False)
print("CSV file updated with standardized match pairs.")
