import csv
import json
import pprint
import datetime
from datetime import datetime,timedelta
import requests
import pandas as pd
cookies = {
    '_ga': 'GA1.1.1441540192.1706257363',
    '__cf_bm': 'DVOQIqozJJ1r4bqxFsXqglliJm3HU2g_fN7tDlLynMo-1719810364-1.0.1.1-lxSttPjHPbydosMAPaIsBtSsWmy9vyobllV3kgUarP.FevW8AbYC_PRZNemQxS5wUWFRRtg0Y3DM.cOaECwUhg',
    '_gcl_au': '1.1.1794238635.1719810369',
    '_fbp': 'fb.1.1719810369429.543942859938192206',
    'digitainllc-_zldp': 'Kn14J1K36mxzFW5Du6Pdnlxhyb8d94ZCFzHaJli%2FY7mrvJkkZlXXUiclHFK5pmAQT3IUrdIYs4k%3D',
    'digitainllc-_zldt': '7d82b030-55b2-4ff8-919a-ada8e5cb56c4-2',
    '_ga_PZ9TR4ZVB0': 'GS1.1.1719810369.3.0.1719810376.0.0.0',
    '_ga_5D166B8T9Y': 'GS1.1.1719810362.1.1.1719810594.0.0.0',
}
data = (datetime.today()-timedelta(days=4)).strftime('%Y-%m-%d')
#print(data)
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    # 'cookie': '_ga=GA1.1.1441540192.1706257363; __cf_bm=DVOQIqozJJ1r4bqxFsXqglliJm3HU2g_fN7tDlLynMo-1719810364-1.0.1.1-lxSttPjHPbydosMAPaIsBtSsWmy9vyobllV3kgUarP.FevW8AbYC_PRZNemQxS5wUWFRRtg0Y3DM.cOaECwUhg; _gcl_au=1.1.1794238635.1719810369; _fbp=fb.1.1719810369429.543942859938192206; digitainllc-_zldp=Kn14J1K36mxzFW5Du6Pdnlxhyb8d94ZCFzHaJli%2FY7mrvJkkZlXXUiclHFK5pmAQT3IUrdIYs4k%3D; digitainllc-_zldt=7d82b030-55b2-4ff8-919a-ada8e5cb56c4-2; _ga_PZ9TR4ZVB0=GS1.1.1719810369.3.0.1719810376.0.0.0; _ga_5D166B8T9Y=GS1.1.1719810362.1.1.1719810594.0.0.0',
    'priority': 'u=1, i',
    'referer': 'https://stats.sportgenerate.com/sport/table-tennis/?tournament=33714',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'tournament': '33714',
    'date': data,
    'status': '0',
}

response = requests.get('https://stats.sportgenerate.com/api/matches.php', params=params, cookies=cookies, headers=headers).json()
with open (f'{data}.json', "w",encoding='utf -8') as file:
    json.dump(response,file,indent=4,ensure_ascii=False)


with open(f'{data}.json',encoding='utf -8') as file:
    src = json.load(file)

with open(f'{data}.csv', "w", newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(('id','date','match','final_score','PS','S1','S2','player_1','player_2'))
#print(src)
for i in src:
    id = i.get("id")
    date = i.get("date")
    S1 = i.get("S1")
    S2 = i.get("S2")
    final_score = S1 + ":"+ S2
    PS = i.get("PS")
    player_1 = i.get("player_1")
    player_2 =i.get("player_2")
    match  = player_1 + " - " +player_2
    #print(id, date,match,final_score, PS,S1, S2,player_1,player_2)
    with open(f'{data}.csv', "a",newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                id, date,match,final_score, PS,S1, S2,player_1,player_2
            )
        )




# Read the CSV file into a DataFrame, using the first row as the header
df = pd.read_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\2024-07-01.csv')

import pandas as pd

# Define a function to sum the first numbers before the ":" sign
def sum_first_numbers(s):
    pairs = s.split(' - ')
    total_sum = 0
    for pair in pairs:
        a = int(pair.split(':')[1])
        total_sum += a
    return total_sum

# Apply the function to each row of the DataFrame
df['Total P2'] = df.iloc[:,4].apply(sum_first_numbers)
df['Fora_1'] = df['Total P2'] - df['Total P1']
df['Fora_2'] = -(df['Total P2'] - df['Total P1'])
# Write the updated DataFrame back to the CSV file
df.to_csv('2024-06-30.csv', index=False)

print("CSV file has been updated with the sum of first numbers before the ':'.")







