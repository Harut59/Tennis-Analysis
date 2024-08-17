# Define a function to sum the first numbers before the ":" sign

# def compare_and_swap(row):
#     player1 = row['player_1']
#     player2 = row['player_2']
#     total_p1 = row['Total P1']
#     total_p2 = row['Total P2']
#
#     if player1 > player2:
#         # Swap Total P1 and Total P2
#         row['Total P1'] = total_p2
#         row['Total P2'] = total_p1
#
#     return row
#
#
# # Apply the function to each row
# df = df.apply(compare_and_swap, axis=1)
#
# # Print the DataFrame with the swapped totals
# print(df)
# #
# # # Write the updated DataFrame back to the CSV file
# df.to_csv('all.csv', index=False)
#
# print("CSV file has been updated with the sum of first numbers before the ':'.")