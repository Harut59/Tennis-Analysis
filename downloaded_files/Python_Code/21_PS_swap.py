import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\all.csv')


# Define a function to swap individual scores within the score column
def swap_scores(row):
    player1 = row['player_1']
    player2 = row['player_2']
    score = row['PS']

    if pd.isna(score):
        return score

    if player1 > player2:
        # Split the score into individual games
        games = score.split(' - ')
        swapped_games = []

        for game in games:
            if game == '0:0':
                swapped_games.append(game)
            else:
                score1, score2 = game.split(':')
                swapped_games.append(f"{score2}:{score1}")

        return ' - '.join(swapped_games)
    else:
        return score


# Apply the function to create a new column with the swapped scores
df['swapped_PS'] = df.apply(swap_scores, axis=1)

# Save the modified DataFrame back to a CSV file
df.to_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\all.csv', index=False)

print(df)


