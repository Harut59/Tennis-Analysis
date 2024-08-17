import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\2024-07-01.csv')

# Define the function to modify the 'fora' column
def modify_fora(row):
    player1 = row['player_1']
    player2 = row['player_2']
    fora = row['Fora_1']
    if player1 < player2:
        return fora
    else:
        return -fora

# Apply the function to the DataFrame
df['modified_fora'] = df.apply(modify_fora, axis=1)

# Save the updated DataFrame back to a CSV file
df.to_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\2024-06-30.csv', index=False)

print("CSV file updated with modified 'fora' values.")
