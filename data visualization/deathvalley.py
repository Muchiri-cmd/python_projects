import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    
    for index, column_header in enumerate (header_row):
        print(index,column_header)
    
    # Get dates,high and low temperatures from file.
    highs,dates,lows = [],[],[]
    for row in reader:
        try:
            high=int(row[1])
            current_date=datetime.strptime(row[0], "%Y-%m-%d")
            low=int(row[3])
        except:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
   
#plot data
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#format plot
title="Daily high and low temperatures-2014\nDeath Valley,CA"
plt.title(title,fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()