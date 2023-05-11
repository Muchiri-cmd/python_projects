import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate (header_row):
        print(index,column_header)
    
    # Get dates,high and low temperatures from file.
    highs,dates,lows = [],[],[]
    for row in reader:
        high=int(row[1])
        highs.append(high)
        
        current_date=datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        
        low=int(row[3])
        lows.append(low)
   
    #plot data
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red')
    plt.plot(dates,lows,c='blue')
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#format plot
plt.title("Daily high and low temperatures-2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()