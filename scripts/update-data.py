# Scrape data from sites : Gather top sets/pick rates

import requests  # library that allows reading web pages

root_urls = ["https://victoryroadvgc.com/2024-season-calendar/", "https://www.smogon.com/dex/sv/formats/vgc24-regulation-f/"]


# Create request objects of Victory Road calander, write text to file
vr_base = requests.get(root_urls[0])  # Victory Road 2024 Season Calendar page object
f = open("../site-dumps/vr_calander_2024.txt", "w")
f.write(vr_base.text)
f.close()

# Access VR events, find top 10 used Pokemon 
# top_used = []
# for line in vr_base.text:
#
# calculate pick rate

# Write pick rate of top 10 Pokemon to pick-rates.csv, (maybe write top sets to )
# f = open("../data/pick-rates.csv", "?")
# f.write()
# f.close()


# Create request object of Smogon Reg-F info page
smogon_reg_base = requests.get(root_urls[1])  # Smogon current Regulation page object
f = open("../site-dumps/smogon_reg-f.txt", "w")
f.write(vr_base.text)
f.close()

# Access VR events, find top 10 used Pokemon (and sets)
#
#

# Write pick rate of top 10 Pokemon to pick-rates.csv, (maybe write top sets to )
# f = open("../data/pick-rates.csv", "?")
# f.write()
# f.close()



