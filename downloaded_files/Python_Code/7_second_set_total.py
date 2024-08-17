import csv
import json
import pprint
import datetime
from datetime import datetime,timedelta
import requests
import pandas as pd



# Read the CSV file into a DataFrame, using the first row as the header
df = pd.read_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\2024-07-01.csv')

# Define a function to sum the numbers in each row
def sum_numbers(s):

    pairs = s.split(' - ')
    #print(pairs)
    total_sum = 0
    for pair in pairs[1:2]:
        a, b = map(int, pair.split(':'))
        #print(a,b)
        total_sum += a + b
    return total_sum

# Apply the function to each row of the DataFrame
df['second_set_total'] = df.iloc[:,4].apply(sum_numbers)

# Write the updated DataFrame back to the CSV file
df.to_csv('2024-07-01.csv', index=False)

print("CSV file has been updated with sum of numbers.")






