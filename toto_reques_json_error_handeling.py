import json
import csv
from datetime import datetime
from seleniumbase import Driver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Initialize CSV files
# with open(f'downloaded_files/toto_avarage_data_total/avg_total.csv', 'w', newline='', encoding='utf-8') as file_2:
#     writer = csv.writer(file_2)
#     writer.writerow(('Game_ID','avarag_total', 'data', 'N', 'name','Player_1','Player_2', 'current_score'))
# #
# with open('downloaded_files/toto_avarage_data_fora/avg_fora.csv', 'w', newline='', encoding='utf-8') as file_3:
#     writer = csv.writer(file_3)
#     writer.writerow(('Game_ID','avg_fora', 'data', 'N', 'name','Player_1','Player_2', 'current_score',))

count = 0
while True:
    driver = Driver(uc=True)
    try:
        # Navigate to the URL
        driver.get('https://sport.totogaming.com/5cd86a1a-c3bf-431e-be15-5be0ce7e961e/live/getliveevents?sportId=25&checkIsActiveAndBetStatus=false&stakeTypes=1&stakeTypes=702&stakeTypes=2&stakeTypes=3&stakeTypes=37&partnerId=125&langId=2&countryCode=AM')

        print(datetime.now())

        # Retrieve the page source
        src = driver.page_source
        #print(type(src))

        # Optionally, write the page source to a file
        with open(f'downloaded_files/toto_loop_request/nor_request{count}.txt', "w", encoding="utf-8") as file:
            file.write(src)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

    # Parse the page source to extract JSON content
    try:
        with open(f'downloaded_files/toto_loop_request/nor_request{count}.txt', 'r', encoding='utf-8') as file:
            html_string = file.read()

        # Extract the JSON substring
        start_index = html_string.find('{')
        end_index = html_string.rfind('}') + 1
        json_string = html_string[start_index:end_index]

        # Validate the JSON string
        json_string = json_string.strip()
        try:
            json_obj = json.loads(json_string)
        except json.JSONDecodeError:
            print(f"Invalid JSON in file nor_request{count}.txt. Skipping...")
            count += 1
            continue

        # Define the output JSON file path
        output_json_file = f'downloaded_files/toto_loop_output_json_file/output{count}.json'

        # Save the JSON object to a JSON file
        with open(output_json_file, 'w', encoding='utf-8') as f:
            json.dump(json_obj, f, indent=4)

        print(f"JSON data saved to {output_json_file}")

        # Process the JSON data
        with open(output_json_file, 'r', encoding='utf-8') as file:
            src = json.load(file)

        CNT = src.get("CNT")
        for i in CNT:
            if i.get("N")=="World":
                i_id = i.get('Id')
                CL = i.get('CL')
                for j in CL:

                    N = j.get("N")
                    if "Men. Rocket Masters Cup" in N:
                        E = j.get("E")
                        for k in E:
                            game_id = k.get("Id")
                            name = k.get("N")
                            Player_1=k.get("HT")
                            Player_2=k.get("AT")
                            data = k.get('D')
                            start_status = k.get('ES')
                            current_score = k.get("SS")
                            #print(current_score,type(current_score))
                            score_segments = current_score.split(' - ')
                            if score_segments[0] == "0:0":
                                stack_type = k.get("StakeTypes")
                                for m in stack_type:
                                    if m['N'] == "Total":
                                        stack = m["Stakes"]
                                        over_coif_list = []
                                        total = 0
                                        for n in stack:
                                            Result_coificent = n.get("F")
                                            over_coif = n.get("A")
                                            over_ctg = n.get('SN')

                                            if over_ctg == "Over" and (Result_coificent > 1.7 and Result_coificent < 1.9):
                                                over_coif_list.append(over_coif)
                                                total += over_coif
                                        if over_coif_list:
                                            avarag_total = total / len(over_coif_list)
                                            print(game_id,avarag_total, data, N, name, current_score)
                                            with open('downloaded_files/toto_avarage_data_total/avg_total.csv', 'a', newline='', encoding='utf-8') as file_2:
                                                writer = csv.writer(file_2)
                                                writer.writerow((game_id,avarag_total, data, N, name,Player_1,Player_2, current_score))
                                            df = pd.read_csv('downloaded_files/toto_avarage_data_total/avg_total.csv')

                                            # Function to standardize match pairs
                                            def standardize_Players(row):
                                                Player_1 = row['Player_1']
                                                Player_2 = row['Player_2']
                                                if Player_1 < Player_2:
                                                    return f"{Player_1} - {Player_2}"
                                                else:
                                                    return f"{Player_2} - {Player_1}"


                                            # Apply the function to create a new column
                                            df['standardized_Players'] = df.apply(standardize_Players, axis=1)

                                            # Save the DataFrame back to a CSV file

                                            df.to_csv('downloaded_files/toto_avarage_data_total/avg_total.csv',
                                                      index=False)

                                            print("CSV file updated with standardized match pairs.")
                                            df_cleaned = df.drop_duplicates(subset='Game_ID')
                                            df_cleaned.to_csv('downloaded_files/toto_avarage_data_total/avg_total.csv', index=False)


                                            # Function to read the CSV file and insert into MySQL
                                            def insert_csv_to_mysql(file_path, user, password, host, database,
                                                                    table_name):
                                                # Read the CSV file into a DataFrame
                                                df = pd.read_csv(file_path)
                                                print(f"this is the dataframe_  {df}")
                                                # Establish MySQL connection
                                                conn = mysql.connector.connect(
                                                    user=user,
                                                    password=password,
                                                    host=host,
                                                    database=database
                                                )
                                                cursor = conn.cursor()

                                                # Prepare the insert statement
                                                cols = ",".join([str(i) for i in df.columns.tolist()])
                                                print(f" here the  TOTAL cols_  {cols}")
                                                for i, row in df.iterrows():
                                                    print(i,row)
                                                    # Create a SELECT statement to check if the row already exists
                                                    check_query = f"SELECT COUNT(*) FROM {table_name} WHERE "
                                                    check_query += " AND ".join([f"{col} = %s" for col in df.columns])
                                                    cursor.execute(check_query, tuple(row))
                                                    result = cursor.fetchone()
                                                    # sql = f"INSERT INTO {table_name} ({cols}) VALUES (" + "%s," * (
                                                    #             len(row) - 1) + "%s)"
                                                    # cursor.execute(sql, tuple(row))
                                                    if result[0] == 0:  # If the row doesn't exist, insert it
                                                        sql = f"INSERT INTO {table_name} ({cols}) VALUES (" + "%s," * (
                                                                    len(row) - 1) + "%s)"
                                                        cursor.execute(sql, tuple(row))
                                                    else:
                                                        print(f"TOTAL-----------Row {i} already exists. Skipping insertion.")
                                                # Commit the transaction
                                                conn.commit()

                                                # Close the cursor and connection
                                                cursor.close()
                                                conn.close()

                                                print(
                                                    f"Data from {file_path} has been successfully inserted into the {table_name} table in the {database} database.")

                                            mysql_user = 'root'
                                            mysql_password = 'your_password'
                                            mysql_host = 'localhost'
                                            mysql_database = 'new_schema'
                                            mysql_table_name = 'avg_total_in_sql'

                                            # Define the file path
                                            csv_file_path = 'downloaded_files/toto_avarage_data_total/avg_total.csv'
                                            insert_csv_to_mysql(csv_file_path, mysql_user, mysql_password, mysql_host,
                                                                mysql_database, mysql_table_name)

                                    elif m['N'] == "Handicap":
                                        stack = m["Stakes"]
                                        fora_coif_list = []
                                        fora_2_coif_list = []
                                        fora = 0
                                        fora_2 = 0
                                        avg_fora = 0

                                        for n in stack:
                                            fora_Result_coificent = n.get("F")
                                            fora_coif = n.get("A")
                                            fora_ctg = n.get('SN')

                                            if fora_ctg == "Handicap 1":


                                                fora_coif_list.append(fora_coif)
                                                fora += fora_coif
                                                print(f'fora is ={fora},fora_Result_coificent={fora_Result_coificent}')
                                        # elif fora_ctg == "Handicap 2":
                                        #     fora_2_coif_list.append(fora_coif)
                                        #     fora_2+=fora_coif
                                        #     print(f'fora_2 is ={fora_2},fora_Result_coificent={fora_Result_coificent}')

                                        if fora_coif_list:
                                            avg_fora = fora / len(fora_coif_list)
                                            print(game_id,avg_fora, data, N, name,Player_1,Player_2, current_score)
                                            with open('downloaded_files/toto_avarage_data_fora/avg_fora.csv', 'a', newline='', encoding='utf-8') as file_3:
                                                writer = csv.writer(file_3)
                                                writer.writerow((game_id,avg_fora, data, N, name,Player_1,Player_2, current_score))
                                            df = pd.read_csv('downloaded_files/toto_avarage_data_fora/avg_fora.csv')
                                        #stuckkkkkkkkkkkkkkkkkkkkkkkkkkk
                                        # elif fora_2_coif_list:
                                        #     avg_fora_2 = fora_2/len(fora_2_coif_list)
                                        #     df = pd.read_csv('downloaded_files/toto_avarage_data_fora/avg_fora.csv')
                                        #     with open('downloaded_files/toto_avarage_data_fora/avg_fora.csv', 'a', newline='', encoding='utf-8') as file_4:
                                        #         writer = csv.writer(file_4)
                                        #         writer.writerow((game_id,avg_fora, data, N, name,Player_1,Player_2, current_score,avg_fora_2))



                                            # Define the function to modify the 'fora' column
                                            def modify_fora(row):
                                                player1 = row['Player_1']
                                                player2 = row['Player_2']
                                                fora_1 = row['avg_fora']
                                                if player1 < player2:
                                                    return fora_1
                                                else:
                                                    return -fora_1


                                            # Apply the function to the DataFrame
                                            df['modified_fora'] = df.apply(modify_fora, axis=1)

                                            # # Save the updated DataFrame back to a CSV file
                                            df.to_csv(
                                                'downloaded_files/toto_avarage_data_fora/avg_fora.csv',
                                                index=False)
                                            # Function to standardize match pairs
                                            def standardize_Players(row):
                                                Player_1 = row['Player_1']
                                                Player_2 = row['Player_2']
                                                if Player_1 < Player_2:
                                                    return f"{Player_1} - {Player_2}"
                                                else:
                                                    return f"{Player_2} - {Player_1}"


                                            # Apply the function to create a new column
                                            df['standardized_Players'] = df.apply(standardize_Players, axis=1)

                                            # Save the DataFrame back to a CSV file

                                            df.to_csv('downloaded_files/toto_avarage_data_fora/avg_fora.csv',
                                                      index=False)

                                            print("CSV file updated with standardized match pairs.")
                                            df_cleaned = df.drop_duplicates(subset='Game_ID')
                                            df_cleaned.to_csv('downloaded_files/toto_avarage_data_fora/avg_fora.csv',
                                                              index=False)


                                            # Function to read the CSV file and insert into MySQL
                                            def insert_csv_to_mysql(file_path_1, user, password, host, database,
                                                                    table_name):
                                                # Read the CSV file into a DataFrame
                                                df = pd.read_csv(file_path_1)
                                                print(f"this is the dataframe_  {df}")
                                                # Establish MySQL connection
                                                conn = mysql.connector.connect(
                                                    user=user,
                                                    password=password,
                                                    host=host,
                                                    database=database
                                                )
                                                cursor = conn.cursor()

                                                # Prepare the insert statement
                                                cols = ",".join([str(i) for i in df.columns.tolist()])
                                                print(f" here the Fora cols_  {cols}")
                                                for j, row in df.iterrows():
                                                    print(j, row)
                                                    # Create a SELECT statement to check if the row already exists
                                                    check_query = f"SELECT COUNT(*) FROM {table_name} WHERE "
                                                    check_query += " AND ".join([f"{col} = %s" for col in df.columns])
                                                    cursor.execute(check_query, tuple(row))
                                                    result = cursor.fetchone()
                                                    # sql = f"INSERT INTO {table_name} ({cols}) VALUES (" + "%s," * (
                                                    #             len(row) - 1) + "%s)"
                                                    # cursor.execute(sql, tuple(row))
                                                    if result[0] == 0:  # If the row doesn't exist, insert it
                                                        sql = f"INSERT  INTO {table_name} ({cols}) VALUES (" + "%s," * (
                                                                len(row) - 1) + "%s)"
                                                        cursor.execute(sql, tuple(row))
                                                    else:
                                                        print(f" FORA---------Row {j} already exists. Skipping insertion.")
                                                # Commit the transaction
                                                conn.commit()

                                                # Close the cursor and connection
                                                cursor.close()
                                                conn.close()

                                                print(
                                                    f"Data from {file_path_1} has been successfully inserted into the {table_name} table in the {database} database.")


                                            mysql_user = 'root'
                                            mysql_password = yourpassword'
                                            mysql_host = 'localhost'
                                            mysql_database = 'new_schema'
                                            mysql_table_name = 'avg_fora_in_sql'

                                            # Define the file path
                                            csv_file_path_1 = 'downloaded_files/toto_avarage_data_fora/avg_fora.csv'
                                            insert_csv_to_mysql(csv_file_path_1, mysql_user, mysql_password, mysql_host,
                                                                mysql_database, mysql_table_name)
                    else:
                        print("there is no Men. Rocket Masters Cup matches")
            else:
                print("there is no World matches")
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error processing JSON data: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
    #
    count += 1

