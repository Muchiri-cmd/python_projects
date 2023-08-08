import pygal
import csv
import re
#import matplotlib.pyplot as plt

#get data from csv
filename='Number of ChatGPT users recorded over past months.csv'
with open (filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    #print(header_row)

    #for index,column_header in enumerate(header_row):
        #print(index,column_header)

    users,months=[],[]
    #Get user numbers from file 
    for row in reader:
        user_count_str=row[2]
        numerical_value=re.search(r'([\d.]+)', user_count_str).group(1)
        users.append(float(numerical_value) * 1e9 if 'billion' in user_count_str else float(numerical_value) * 1e6)
        months.append(row[1])
        print(users)

#format plot
hist=pygal.Bar()
hist.title="Number of CHATGPT users"
hist.x_labels=months
hist.x_title="Months"
hist.y_title="Users"

hist.add('users',users)

hist.render_to_file('users.svg')
