import datetime
from datetime import timedelta
import csv
import json
import pprint
import datetime
from datetime import datetime,timedelta
import requests
import pandas as pd
from datetime import datetime,time
import asyncio

while True:
    # group = " "
    # group_name = " "
    # # Specific date and time
    # def check_time():
    #     global group, group_name
    #     if datetime.now().time() < time(15,14):
    #         group = "33714"
    #         group_name = "Men. Rocket Masters Cup"
    #     elif  time(15,14) < datetime.now().time() < time(17,45):
    #         group = "41980"
    #         group_name = "Men. Rocket Masters Cup.SP"
    #     elif time(17,45) < datetime.now().time() < time(20,15):
    #         group = "47939"
    #         group_name = "Men. Rocket Masters Cup.SP1"
    #     elif  datetime.now().time() > time(20, 15):
    #         group = "47940"
    #         group_name = "Men. Rocket Masters Cup.SP2"
    #     else:
    #
    #         print("error")
    #         return 0
    # check_time()

    # print(group,group_name)
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

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
        # 'cookie': '_ga=GA1.1.1441540192.1706257363; __cf_bm=DVOQIqozJJ1r4bqxFsXqglliJm3HU2g_fN7tDlLynMo-1719810364-1.0.1.1-lxSttPjHPbydosMAPaIsBtSsWmy9vyobllV3kgUarP.FevW8AbYC_PRZNemQxS5wUWFRRtg0Y3DM.cOaECwUhg; _gcl_au=1.1.1794238635.1719810369; _fbp=fb.1.1719810369429.543942859938192206; digitainllc-_zldp=Kn14J1K36mxzFW5Du6Pdnlxhyb8d94ZCFzHaJli%2FY7mrvJkkZlXXUiclHFK5pmAQT3IUrdIYs4k%3D; digitainllc-_zldt=7d82b030-55b2-4ff8-919a-ada8e5cb56c4-2; _ga_PZ9TR4ZVB0=GS1.1.1719810369.3.0.1719810376.0.0.0; _ga_5D166B8T9Y=GS1.1.1719810362.1.1.1719810594.0.0.0',
        'priority': 'u=1, i',
        'referer': f'https://stats.sportgenerate.com/sport/table-tennis/?tournament=33714',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    today = datetime.today()
    #print(today)
    with open('all_sport_gen_site.csv', "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(('id', 'date', 'Players_names', 'final_score', 'Total_Score', 'S1', 'S2', 'player_1', 'player_2','group_name'))
    days_later = today - timedelta(days=1)




    for i in range(1,365):
        days_later = (today - timedelta(i)).strftime('%Y-%m-%d')
        print(f"{i} later:", days_later)
        params = {
            'tournament': 33714,
            'date': days_later,
            'status': '0',
        }

        response = requests.get('https://stats.sportgenerate.com/api/matches.php', params=params, cookies=cookies, headers=headers).json()
        directory = 'sport_generate_site_json'
        with open (f'downloaded_files/{directory}/{days_later}.json', "w",encoding='utf -8') as file:
            json.dump(response,file,indent=4,ensure_ascii=False)

        with open(f'downloaded_files/{directory}/{days_later}.json',encoding='utf -8') as file:
            src = json.load(file)


        #print(src)
        for j in src:
            group_name= "fiurst"
            id = j.get("id")
            date = j.get("date")
            S1 = j.get("S1")
            S2 = j.get("S2")
            final_score = S1 + ":"+ S2
            # print(final_score)
            Total_Score = j.get("PS")
            if Total_Score =="" or Total_Score ==" ":
                continue
            # print(Total_Score)
            player_1 = j.get("player_1")
            player_2 =j.get("player_2")
            Players_names  = player_1 + " - " +player_2
            print(id,date,Players_names,final_score,Total_Score,S1, S2,player_1,player_2,group_name)
            with open('all_sport_gen_site.csv', "a",newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        id,date,Players_names,final_score,Total_Score,S1, S2,player_1,player_2,group_name
                    )
                )

    #
    # # #----------------------------------2_change_match_place.py-----------------------
    df = pd.read_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\all_sport_gen_site.csv')

    # Function to standardize match pairs
    def standardize_match(row):

        player1 = row['player_1']
        player2 = row['player_2']
        if player1 < player2:
            return f"{player1} - {player2}"
        else:
            return f"{player2} - {player1}"

    print("before")
    # Apply the function to create a new column
    df['standardized_match'] = df.apply(standardize_match, axis=1)
    print('after')
    # Save the DataFrame back to a CSV file

    df.to_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\all_sport_gen_site.csv', index=False)

    print("CSV file updated with standardized match pairs.")
    #
    # #------------------------------3_Total_match.py----------------------------
    #Define a function to sum the numbers in each row
    import pandas as pd



    def sum_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        if not isinstance(s, str):  # Check if the value is not a string
            return 0
        try:
            # Remove any leading/trailing spaces
            s = s.strip()
            # Split the string by ' - ' to get the pairs
            pairs = s.split(' - ')
            total_sum = 0
            for pair in pairs:
                # Ensure the pair is in the correct 'a:b' format
                if ':' in pair:
                    a, b = map(int, pair.split(':'))
                    total_sum += a + b
                else:
                    print(f"Unexpected format in pair '{pair}'")
                    continue
            return total_sum
        except Exception as e:
            print(f"Error processing input '{s}': {e}")
            return 0


    # Example usage with a DataFrame
    df = pd.read_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\all_sport_gen_site.csv')
    df['Total'] = df.iloc[:, 4].apply(sum_numbers)
    df.to_csv(r'C:\Users\Harut\PycharmProjects\SportGenerateTenis\all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with the sum of numbers.")


    #
    # def sum_numbers(s):
    #     if pd.isna(s):  # Check if the value is NaN
    #         return 0
    #     if not isinstance(s, str):  # Check if the value is not a string
    #         return 0
    #     try:
    #         pairs = s.split(' - ')
    #         total_sum = 0
    #         for pair in pairs:
    #             a, b = map(int, pair.split(':'))
    #             total_sum += a + b
    #         return total_sum
    #     except Exception as e:
    #         print(f"Error processing input '{s}': {e}")
    #         return 0
    #
    # # Example usage with a DataFrame
    # # Assuming df is your DataFrame and the column of interest is the fifth column (index 4)
    # df['Total'] = df.iloc[:, 4].apply(sum_numbers)
    # df.to_csv('all_sport_gen_site.csv', index=False)
    #
    # print("CSV file has been updated with sum of numbers.")

    #####
    # def sum_numbers(s):
    #     print(type(s))
    #     if pd.isna(s):  # Check if the value is NaN
    #         return 0
    #     # pairs = s.split(' - ')
    #     pairs = s
    #     print(pairs)
    #     total_sum = 0
    #     for pair in pairs:
    #         a, b = map(int, pair.split(':'))
    #         # print(a,b)
    #         total_sum += a + b
    #         # print(total_sum)
    #     return total_sum
    #
    # # Apply the function to each row of the DataFrame
    # df['Total'] = df.iloc[:,4].apply(sum_numbers)
    #
    # # Write the updated DataFrame back to the CSV file
    # df.to_csv('all_sport_gen_site.csv', index=False)
    #
    # print("CSV file has been updated with sum of numbers.")

    # #-----------------------4_totalP1.py-------------------
    # # Define a function to sum the first numbers before the ":" sign
    def sum_first_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        if not isinstance(s, str):  # Check if s is not a string
            return 0
        pairs = s.split(' - ')
        total_sum = 0
        for pair in pairs:
            try:
                a = int(pair.split(':')[0])
                total_sum += a
            except (ValueError, IndexError):
                print(f"Skipping pair due to invalid format: '{pair}'")
                continue
        return total_sum

    # Apply the function to each row of the DataFrame
    df['Total P1'] = df.iloc[:,4].apply(sum_first_numbers)

    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with the sum of first numbers before the ':'.")
    #
    # #-----------------------5_totalP2.py and fora1, fora2-------------------
    #
    # Define a function to sum the first numbers before the ":" sign
    # def sum_first_numbers(s):
    #     if pd.isna(s):  # Check if the value is NaN
    #         return 0
    #     pairs = s.split(' - ')
    #     total_sum = 0
    #     for pair in pairs:
    #         a = int(pair.split(':')[1])
    #         total_sum += a
    #     return total_sum
    #
    # # Apply the function to each row of the DataFrame
    # df['Total P2'] = df.iloc[:,4].apply(sum_first_numbers)
    # ------------------------
    def sum_first_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        if not isinstance(s, str):  # If s is not a string, return 0
            return 0
        total_sum = 0
        try:
            pairs = s.split(' - ')
            for pair in pairs:
                parts = pair.split(':')
                if len(parts) == 2 and parts[1].isdigit():  # Ensure there are two parts and the second part is a digit
                    a = int(parts[1])
                    total_sum += a
        except Exception as e:
            print(f"Error processing input '{s}': {e}")
            return 0
        return total_sum

    # Example usage with a DataFrame
    # Assuming df is your DataFrame and the column of interest is the fifth column (index 4)
    df['Total P2'] = df.iloc[:, 4].apply(sum_first_numbers)


    df['Fora_1'] = df['Total P2'] - df['Total P1']
    df['Fora_2'] = -(df['Total P2'] - df['Total P1'])
    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with the sum of first numbers before the ':'.")
    # #------------------------------6_first_set_total.py-------------------------
    # Define a function to sum the numbers in each row
    # def sum_numbers(s):
    #     if pd.isna(s):  # Check if the value is NaN
    #         return 0
    #     pairs = s.split(' - ')
    #     #print(pairs)
    #     total_sum = 0
    #     for pair in pairs[:1]:
    #         a, b = map(int, pair.split(':'))
    #         #print(a,b)
    #         total_sum += a + b
    #     return total_sum
    #
    # # Apply the function to each row of the DataFrame
    # df['first_set_total'] = df.iloc[:,4].apply(sum_numbers)
    # -------------------
    def first_set_total(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        if not isinstance(s, str):  # If s is not a string, return 0
            return 0
        total_sum = 0
        try:
            pairs = s.split(' - ')
            for pair in pairs[:1]:
                parts = pair.split(':')
                if len(parts) == 2 and parts[1].isdigit():  # Ensure there are two parts and the second part is a digit
                    # a = int(parts[1])
                    a, b = map(int, pair.split(':'))
                    total_sum += a +b
        except Exception as e:
            print(f"Error processing input '{s}': {e}")
            return 0
        return total_sum

    # Example usage with a DataFrame
    # Assuming df is your DataFrame and the column of interest is the fifth column (index 4)
    df['first_set_total'] = df.iloc[:, 4].apply(first_set_total)


    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with sum of numbers.")

    # #------------------------------7_second_set_total.py-------------------------
    # Define a function to sum the numbers in each row
    def sum_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
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
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with sum of numbers.")
    # #------------------------------8_third_set_total.py-------------------------
    # Define a function to sum the numbers in each row
    def sum_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        pairs = s.split(' - ')
        #print(pairs)
        total_sum = 0
        for pair in pairs[2:3]:
            a, b = map(int, pair.split(':'))
            #print(a,b)
            total_sum += a + b
        return total_sum

    # Apply the function to each row of the DataFrame
    df['third_set_total'] = df.iloc[:,4].apply(sum_numbers)

    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with sum of numbers.")

    # #------------------------------9_fourth_set_total.py-------------------------
    # Define a function to sum the numbers in each row
    def sum_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        pairs = s.split(' - ')
        #print(pairs)
        total_sum = 0
        for pair in pairs[3:4]:
            a, b = map(int, pair.split(':'))
            #print(a,b)
            total_sum += a + b
        return total_sum

    # Apply the function to each row of the DataFrame
    df['fourth_set_total'] = df.iloc[:,4].apply(sum_numbers)

    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with sum of numbers.")

    # #------------------------------10_fifth_set_total.py-------------------------
    # Define a function to sum the numbers in each row
    def sum_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        pairs = s.split(' - ')
        #print(pairs)
        total_sum = 0
        for pair in pairs[4:5]:
            a, b = map(int, pair.split(':'))
            #print(a,b)
            total_sum += a + b
        return total_sum

    # Apply the function to each row of the DataFrame
    df['fifth_set_total'] = df.iloc[:,4].apply(sum_numbers)

    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)
    print("CSV file has been updated with sum of numbers.")
    # #------------------------------11_first_set_fora.py-------------------------


    def sum_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        if not isinstance(s, str):  # If s is not a string, return 0
            return 0
        pairs = s.split(' - ')
        total_sum = 0
        for pair in pairs[:1]:
            try:
                parts = pair.split(':')
                if len(parts) == 2:
                    a = int(parts[0])
                    b = int(parts[1])
                    total_sum = -(a - b)
            except ValueError as e:
                print(f"Error processing pair '{pair}': {e}")
                return 0
        return total_sum

    # Example usage with a DataFrame
    # Assuming df is your DataFrame and the column of interest is the fifth column (index 4)
    df['first_set_fora'] = df.iloc[:, 4].apply(sum_numbers)

    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)
    print("CSV file has been updated with sum of numbers.")

    # --------------------------------------
    # Define a function to sum the numbers in each row
    # def sum_numbers(s):
    #     if pd.isna(s):  # Check if the value is NaN
    #         return 0
    #     pairs = s.split(' - ')
    #     #print(pairs)
    #     total_sum = 0
    #     for pair in pairs[:1]:
    #         a, b = map(int, pair.split(':'))
    #         #print(a)
    #         total_sum = -(a - b)
    #     return total_sum
    #
    # # # Apply the function to each row of the DataFrame
    # df['first_set_fora'] = df.iloc[:,4].apply(sum_numbers)
    #
    # # Write the updated DataFrame back to the CSV file
    # df.to_csv('all_sport_gen_site.csv', index=False)
    # print("CSV file has been updated with sum of numbers.")
    # # # #------------------------------12_second_set_fora.py-------------------------
    # Define a function to sum the numbers in each row
    def sum_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        pairs = s.split(' - ')
        #print(pairs)
        total_sum = 0
        for pair in pairs[1:2]:
            a, b = map(int, pair.split(':'))
            #print(a)
            total_sum = -(a - b)
        return total_sum

    # # Apply the function to each row of the DataFrame
    df['second_set_fora'] = df.iloc[:,4].apply(sum_numbers)

    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with sum of numbers.")
    # #------------------------------13_thirtd_set_fora.py-------------------------
    #
    # Define a function to sum the numbers in each row
    def sum_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        pairs = s.split(' - ')
        #print(pairs)
        total_sum = 0
        for pair in pairs[2:3]:
            a, b = map(int, pair.split(':'))
            #print(a)
            total_sum = -(a - b)
        return total_sum

    # # Apply the function to each row of the DataFrame
    df['third_set_fora'] = df.iloc[:,4].apply(sum_numbers)

    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with sum of numbers.")

    # #------------------------------14_fourth_set_fora.py-------------------------
    # Define a function to sum the numbers in each row
    def sum_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        pairs = s.split(' - ')
        #print(pairs)
        total_sum = 0
        for pair in pairs[3:4]:
            a, b = map(int, pair.split(':'))
            #print(a)
            total_sum = -(a - b)
        return total_sum

    # # Apply the function to each row of the DataFrame
    df['fourth_set_fora'] = df.iloc[:,4].apply(sum_numbers)

    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with sum of numbers.")

    # #------------------------------15_fifth_set_fora.py-------------------------
    # Define a function to sum the numbers in each row
    def sum_numbers(s):
        if pd.isna(s):  # Check if the value is NaN
            return 0
        pairs = s.split(' - ')
        #print(pairs)
        total_sum = 0
        for pair in pairs[4:5]:
            a, b = map(int, pair.split(':'))
            #print(a)
            total_sum = -(a - b)
        return total_sum

    # # Apply the function to each row of the DataFrame
    df['fifth_set_fora'] = df.iloc[:,4].apply(sum_numbers)

    # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with sum of numbers.")
    # #-----------------------16_standardized_fora.py----------------------------
    # Define the function to modify the 'fora' column
    def modify_fora(row):
        player1 = row['standardized_match']
        player2 = row['player_2']
        fora = row['Fora_1']
        if player1 < player2:
            return fora
        else:
            return -fora

    # Apply the function to the DataFrame
    df['modified_fora'] = df.apply(modify_fora, axis=1)

    # Save the updated DataFrame back to a CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file updated with modified 'fora' values.")
    # # # -----------------------17_swap total---------------------------------
    # Define a function to sum the first numbers before the ":" sign

    def compare_and_swap(row):
        player1 = row['player_1']
        player2 = row['player_2']
        total_p1 = row['Total P1']
        total_p2 = row['Total P2']

        if player1 > player2:
            # Swap Total P1 and Total P2
            row['Total P1'] = total_p2
            row['Total P2'] = total_p1

        return row


    # Apply the function to each row
    df = df.apply(compare_and_swap, axis=1)

    # Print the DataFrame with the swapped totals
    print(df)
    #
    # # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with the sum of first numbers before the ':'.")
    # #----------------------------18_Fora_1_Fora2_swap.py----------------------------
    def compare_and_swap(row):
        player1 = row['player_1']
        player2 = row['player_2']
        fora_p1 = row['Fora_1']
        fora_p2 = row['Fora_2']

        if player1 > player2:
            # Swap Total P1 and Total P2
            row['Fora_1'] = fora_p2
            row['Fora_2'] = fora_p1

        return row


    # Apply the function to each row
    df = df.apply(compare_and_swap, axis=1)

    # Print the DataFrame with the swapped totals
    print(df)
    #
    # # Write the updated DataFrame back to the CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with the sum of first numbers before the ':'.")
    # #-----------------------19_all_sets_fora_standarlized.py------------------
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
    df.to_csv('all_sport_gen_site.csv', index=False)

    print("CSV file has been updated with the sum of first numbers before the ':'.")
    #
    # # #--------------------20_final_score_swap-----------------------------------
    # Define a function to swap the score
    def swap_score(row):
        player1 = row['player_1']
        player2 = row['player_2']
        score = row['final_score']

        # Swap the score if player1 is greater than player2
        if player1 > player2:
            score1, score2 = score.split(':')
            row['final_score'] = f"{score2}:{score1}"

        return row


    # Apply the function to the DataFrame
    df = df.apply(swap_score, axis=1)

    # Save the modified DataFrame back to a CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)

    # #-----------------------21_PS_swap.py----------------------------------------
    #
    # # # Define a function to swap individual scores within the score column
    def swap_scores(row):
        player1 = row['player_1']
        player2 = row['player_2']
        score = row['Total_Score']

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
    df['swapped_Total_score'] = df.apply(swap_scores, axis=1)

    # Save the modified DataFrame back to a CSV file
    df.to_csv('all_sport_gen_site.csv', index=False)
    #-----------------------------22_group_by match_last_10_row.py
    # Load the data
    df = pd.read_csv('all_sport_gen_site.csv')
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


    async def do_something():
        print("Doing something...")

        # Pause for 2 seconds using asyncio.sleep and await it
        await asyncio.sleep(2*60*60)


    # Run the async function
    asyncio.run(do_something())
    #time.sleep(2 * 60 * 60)
    # time.sleep(2)
    print("2 hours have passed.")
