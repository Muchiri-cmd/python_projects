import csv
import csv 
import pygal
from pygal.maps.world import World
from countrycodes import get_country_code

filename='API_FB.BNK.CAPA.ZS_DS2_en_csv_v2_5360955.csv'
with open(filename,mode='r')as f:
    reader=csv.DictReader(f)
    header_row=next(reader)
    info_dict={}
    
    for  lines in reader :
        print(lines)
    