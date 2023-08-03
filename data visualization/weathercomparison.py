import csv
from datetime import datetime
import matplotlib.pyplot as plt 

def get_weather_data(filename, dates, highs, lows, date_index, high_index,
        low_index):
    #Get the highs and lows from a data file.
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, and high and low temperatures from the file.
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except :
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
                
# Get weather data for Sitka.
filename = 'sitka_weather_2014.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=0, high_index=5,
        low_index=6)

#set display figure parameters
fig=plt.figure(dpi=128,figsize=(10,6))

# Plot Sitka weather data.
plt.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# Get weather data for Death Valley.
filename = 'death_valley_2014.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=0, high_index=4,
        low_index=5)

#plot weather for Death valley
plt.plot(dates,highs,c='red',alpha=0.6)
plt.plot(dates,lows,c='blue',alpha=0.6)

#format plot 
plt.title='Daily high and low temperature \nComparison between Sitka and Death valley'
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
