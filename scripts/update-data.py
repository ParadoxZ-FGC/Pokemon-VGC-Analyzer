# Scrape data from sites : Gather top sets/pick rates

import requests  # library that allows reading web pages
import re

root_urls = ["https://victoryroadvgc.com/2024-season-calendar/",
             "https://www.smogon.com/dex/sv/formats/vgc24-regulation-f/"]
events = ["https://victoryroadvgc.com/2024-charlotte/"]

# Create request objects of Victory Road calendar, write text to file
vr_base = requests.get(events[0])  # Victory Road 2024 Season Calendar page object
with open("vr_calander_2024.txt", "w", encoding="utf-8") as f:
    f.write(vr_base.text)
f.close()

# Access VR events, find usage # of Pokemon
top_used = {"Name": 0}
lines = open("vr_calander_2024.txt", "r", encoding="utf-8").readlines()
for line in lines:
    if "https://victoryroadvgc.com/wp-content/uploads/sprites/" in line:
        mons_list = re.findall('title="([^"]*)"', line)
        for mon_name in mons_list:
            all_pokemon = open("pokemon.txt", "r", encoding="utf-8").readlines()
            for pokemon in all_pokemon:
                if mon_name in pokemon:
                    update = False
                    for top_used_mon in top_used:
                        if mon_name == top_used_mon:
                            top_used[mon_name] += 1
                            update = True
                    if not update:
                        top_used[mon_name] = 1

# Calculate % usage of mons
no_teams = 128
mon_percents = {}
for mon in top_used:
    mon_percents[mon] = (top_used[mon] / no_teams) * 100

# Write % pick rate of Pokemon to pick-rates.csv
f = open("pick-rates.csv", "a")
for mon in mon_percents:
    f.write(f"{mon},{'{:.1f}'.format(mon_percents[mon])}%\n")
f.close()



# Create request object of Smogon Reg-F info page
smogon_reg_base = requests.get(root_urls[1])  # Smogon current Regulation page object
with open("smogon_reg-f.txt", "w", encoding="utf-8") as f:
    f.write(smogon_reg_base.text)
f.close()

# Access VR events, find top 10 used Pokemon (and sets)
#
#

# Write pick rate of top 10 Pokemon to pick-rates.csv, (maybe write top sets to )
# f = open("../data/pick-rates.csv", "?")
# f.write()
# f.close()
