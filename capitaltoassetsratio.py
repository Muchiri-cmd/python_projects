import csv 
import pygal
from pygal.maps.world import World
from countrycodes import get_country_code

info_dict={}

filename='API_FB.BNK.CAPA.ZS_DS2_en_csv_v2_5360955.csv'
with open(filename,mode='r')as f:
    reader=csv.DictReader(f)
    header_row=next(reader)
    
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    for row in reader:
            country_name=row['Country Name']
            ratio = row['2021']
            code=get_country_code(country_name)
            if code and ratio:
                info_dict[code]=float(ratio)

           
#World map
world_map = pygal.maps.world.World()
world_map.title = 'Bank Capital to Assets Ratio'
world_map.add('Bank capital to assets ratio (%)', info_dict)
world_map.render_to_file('bankcapitaltoassetsratio.svg')
        
        

    
