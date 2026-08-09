from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime 

path=Path('weather_data/ktm_daily_weather.csv')
lines=path.read_text().splitlines()# yesley list of lines dinxa

reader=csv.reader(lines)#reader() ley tyo list lai parse garxa
header_row=next(reader)# next() ley arko line return garxa, 
# tara yaa ekchoti maatra call gareko xu so ekchoti maatra line return garxa jun
# header line hunxa jun chai header_row maa gayera basxa ani teslai display garako

# use the below code to see the index of header
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

high_temps=[]
low_temps=[]
dates=[]
for row in reader:#pailaa reader ley header padi sakeko vayera 
    # aba chai arko line baata suru hunxa, first line xodera
    #second line baata loop suru hunxa
    current_dates=datetime.strptime(row[0],'%Y-%m-%d')#datetime object maa conversion gareko
    high=float(row[1])#string lai float maa convert gareko
    low=float(row[2])
    dates.append(current_dates)
    high_temps.append(high)
    low_temps.append(low)

# print(high_temps[:20])
# print(low_temps[:20])

plt.style.use('Solarize_Light2')
fig, ax=plt.subplots()
ax.plot(dates[:100], high_temps[:100], color='red')
ax.plot(dates[:100], low_temps[:100], color='cyan')
ax.fill_between(dates[:100], high_temps[:100], low_temps[:100], facecolor='gray', alpha=0.3)

ax.set_title('Kathmandu Daily temperature', fontsize=24)
ax.set_xlabel('Dates', fontsize=16)
fig.autofmt_xdate()#dates lai diagonally draw garna lai, so overlapping nahos
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()