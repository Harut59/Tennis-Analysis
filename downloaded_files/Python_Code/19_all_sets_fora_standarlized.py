import datetime
from datetime import timedelta
import csv
import json
import pprint
import datetime
from datetime import datetime,timedelta
import requests
import pandas as pd
from datetime import datetime, timedelta
df = pd.read_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\all.csv')
def compare_and_swap(row):
    player1 = row['player_1']
    player2 = row['player_2']
    #first_set_fora_p1 = row['first_set_fora']


    if player1 > player2:
        # Swap Total P1 and Total P2
        row['first_set_fora'] = -(row['first_set_fora'])
        row['second_set_fora'] = -(row['second_set_fora'])
        row['third_set_fora'] = -(row['third_set_fora'])
        row['fourth_set_fora'] =-(row['fourth_set_fora'])
        row['fifth_set_fora'] =-(row['fifth_set_fora'])
    return row


# Apply the function to each row
df = df.apply(compare_and_swap, axis=1)

# Print the DataFrame with the swapped totals
print(df)
#
# # Write the updated DataFrame back to the CSV file
df.to_csv('all.csv', index=False)

print("CSV file has been updated with the sum of first numbers before the ':'.")