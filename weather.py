from pathlib import Path
import csv

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
for row in reader:#pailaa reader ley header padi sakeko vayera 
    # aba chai arko line baata suru hunxa, first line xodera
    #second line baata loop suru hunxa
    high=float(row[1])#string lai float maa convert gareko
    low=float(row[2])
    high_temps.append(high)
    low_temps.append(low)

print(high_temps[:20])
print(low_temps[:20])