import csv 
import pygal
from pygal.maps.world import World
from countrycodes import get_country_code

filename = 'API_FB.BNK.CAPA.ZS_DS2_en_csv_v2_5360955.csv'

with open(filename) as f:
    reader = csv.DictReader(f)
    header_row = next(reader)
    info_dict = {}

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    """Write
    a program that generates a dictionary with Pygal’s two-letter country codes
    as its keys and your chosen data from the file as its values. Plot the data on a
    Worldmap and style the map as you like."""

    for row in reader:
        code = get_country_code(row['Country Name'])
        ratio = int(float(row['Bank capital to assets ratio (%)']))
        info_dict[code] = ratio

# Create a world map
world_map = pygal.maps.world.World()
# Set the title of the map
world_map.title = 'Bank Capital to Assets Ratio'
# Add the bank capital to assets ratio data to the map
world_map.add('Bank capital to assets ratio (%)', info_dict)
# Save the map to an SVG file
world_map.render_to_file('bankcapitaltoassetsratio.svg')
