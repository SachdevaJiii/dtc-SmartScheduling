import csv
import pandas as pd
print('Greetings!\nWelcome to DTC!\nPlease enter your source and destination.')

#Taking user input
s=input('Please enter the source:')
d=input('Please enter the destination:')


#Fetching the route

data = pd.read_csv('D:\SIH 2024\dtc-SmartScheduling\Recommend system\Route 761.csv')
column_list = data['stop'].tolist()
if s in column_list:
    if d in column_list:
        print('You can travel in bus number 761 for your journey')
    else:
        print('Sorry there are no direct busses available.')
else:
    print('Sorry there are no direct busses available.')
# print(column_list)


#Test Output
# print(s)
# print(d)