# Scrape data from sites : Gather top sets/pick rates

import requests  # library that allows reading web pages

root_urls = ["https://victoryroadvgc.com/2024-season-calendar/", "https://www.smogon.com/dex/sv/formats/vgc24-regulation-f/"]
events = ["https://victoryroadvgc.com/2024-charlotte/"]


# Create request objects of Victory Road calander, write text to file
vr_base = requests.get(root_urls[0])  # Victory Road 2024 Season Calendar page object
f = open("../site-dumps/vr_calander_2024.txt", "w")
f.write(vr_base.text)
f.close()

# Access VR events, find top 10 used Pokemon 
top_used = {}
for line in requests.get(events[0]).text:
  if line includes "https://victoryroadvgc.com/wp-content/uploads/sprites/":
    #mon_on_line = read up to title
    for mon in top_used:
      if mon_on_line = mon:
        top_used[mon] += 1
      else:
        top_used[mon] = 1
# no_teams = find top place number
mon_percents = {}
for mon in top_used:
  mon_percents[mon] = (top_used[mon] / no_teams) * 10
  
# Write pick rate of top 10 Pokemon to pick-rates.csv
f = open("../data/pick-rates.csv", "a")
for mon in mon_percents:
  f.write(f"{mon},{mon_percents[mon]}%") # Need to add role gathering
f.close()


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



