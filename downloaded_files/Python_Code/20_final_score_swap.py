import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\all.csv')


# Define a function to swap the score
def swap_score(row):
    player1 = row['player_1']
    player2 = row['player_2']
    score = row['score']

    # Swap the score if player1 is greater than player2
    if player1 > player2:
        score1, score2 = score.split(':')
        row['score'] = f"{score2}:{score1}"

    return row


# Apply the function to the DataFrame
df = df.apply(swap_score, axis=1)

# Save the modified DataFrame back to a CSV file
df.to_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\all.csv', index=False)

print(df)
