from pathlib import Path
import csv

path=Path('weather_data/climate.csv')
lines=path.read_text().splitlines()# yesley list of lines dinxa

reader=csv.reader(lines)#reader() ley tyo list lai parse garxa
header_row=next(reader)# next() ley arko line return garxa, 
# tara yaa ekchoti maatra call gareko xu so ekchoti maatra line return garxa jun
# header line hunxa jun chai header_row maa gayera basxa ani teslai display garako
print(header_row)