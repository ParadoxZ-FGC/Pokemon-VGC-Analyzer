# Scrape data from sites : Gather top Pokemon pick rates/sets

import requests  # library that allows reading web pages
import re

root_urls = ["https://victoryroadvgc.com/2024-season-calendar/",
             "https://www.smogon.com/dex/sv/formats/vgc24-regulation-f/"]
events = ["https://victoryroadvgc.com/2024-charlotte/"]

# Create request objects of Victory Road calendar and Smogon Reg-F info page, write text to file
vr_base = requests.get(events[0])  # Victory Road 2024 Season Calendar page object
with open("../site-dumps/vr_calendar_2024.txt", "w", encoding="utf-8") as vr:
    vr.write(vr_base.text)
vr.close()
smogon_reg_base = requests.get(root_urls[1])  # Smogon current Regulation page object
with open("../site-dumps/smogon_reg-f_info.txt", "w", encoding="utf-8") as s:
    s.write(smogon_reg_base.text)
s.close()

# Access VR events -> find usage # of Pokemon -> Calculate % usage of mons -> Write % pick rate of Pokemon to pick-rates.csv
top_used = {"Pokemon": 0}
percent_use = {}
no_teams = 128

vr_lines = open("../site-dumps/vr_calendar_2024.txt", "r", encoding="utf-8").readlines()
for line in vr_lines:
    if "https://victoryroadvgc.com/wp-content/uploads/sprites/" in line:
        mons_list = re.findall('title="([^"]*)"', line)
        for mon_name in mons_list:
            all_pokemon = open("../txt-lists/pokemon.txt", "r", encoding="utf-8").readlines()
            for pokemon in all_pokemon:
                if mon_name in pokemon:
                    mon_update = False
                    for top_used_mon in top_used:
                        if mon_name == top_used_mon:
                            top_used[mon_name] += 1
                            mon_update = True
                    if not mon_update:
                        top_used[mon_name] = 1
print("Successfully: Accessed Victory Road calendar events and found usage # of Pokemon")

for mon in top_used:
    percent_use[mon] = (top_used[mon] / no_teams) * 100
print("Successfully: Calculated usage % of Pokemon")

with open("../data/pick-rates.csv", "w", encoding="utf-8") as pr:
    for mon in percent_use:
        pr.write(f"{mon},{'{:.1f}'.format(percent_use[mon])}%\n")
pr.close()
print("Successfully: Wrote data to pick-rates.csv")


# Access Smogon -> Find top mons that have sets -> Find sets for top mons -> Write to top-sets.csv
top_mons_w_sets = {"Amoonguss": "https://www.smogon.com/dex/sv/pokemon/amoonguss/vgc24-regulation-f/"}
top_mon_sets = {"Pokemon": ["Set No.", "Role", "Item", "Ability", "Tera Type", "EVs", "IVs", "Nature", "Move 1", "Move 2", "Move 3", "Move 4", "Counters"],
                "Incineroar": [1, "Bulky Support", "Rocky Helmet", "Intimidate", "Grass", "252/252/0/0/4/0", "31/31/31/31/31/31", "Adamant", "Flare Blitz", "Knock Off", "Fake Out", "Parting Shot", "Ogerpon"]}

s_lines = open("../site-dumps/smogon_reg-f_info.txt", "r", encoding="utf-8").readlines()
for line in s_lines:
    if "pokemon_with_strategies" in line:
        mons_w_sets = re.findall('"([^"]*)"', re.findall(r'"pokemon_with_strategies":\[([^\[]*)]', line)[0])
        for mon_w_set in mons_w_sets:
            for mon in top_used:
                if mon_w_set in mon:
                    top_mons_w_sets[mon] = f"https://www.smogon.com/dex/sv/pokemon/{mon.lower()}/vgc24-regulation-f/"
print("Successfully: Accessed Smogon Regulation F page and found top used Pokemon with sets")

for mon in top_mons_w_sets:
    with open(f"../smogon-dumps/{mon.lower()}.txt", "w", encoding="utf-8") as new_mon:
        new_mon.write(requests.get(top_mons_w_sets[mon]).text)
    new_mon.close()
    new_mon_lines = open(f"../smogon-dumps/{mon.lower()}.txt", "r", encoding="utf-8").readlines()
    for line in new_mon_lines:
        if '"format":"VGC24 Regulation F"' in line:
            split_line = re.split('"format":"VGC24 Regulation F"', line)[1]
            role = re.findall('"movesets":.."name":"([^"]*)"', split_line)[0]
            items = "/".join(re.findall('"([^"]*)"', re.findall(r'"items":\[([^\[]*)]', split_line)[0]))
            abilities = "/".join(re.findall('"([^"]*)"', re.findall(r'"abilities":\[([^\[]*)]', split_line)[0]))
            teras = "/".join(re.findall('"([^"]*)"', re.findall(r'"teratypes":\[([^\[]*)]', split_line)[0]))
            hp = re.findall('"hp":([^"]*),', split_line)[0:2]
            if len(hp) == 1:
                hp.append(31)
            ph_atk = re.findall('"atk":([^"]*),', split_line)[0:2]
            if len(ph_atk) == 1:
                ph_atk.append(31)
            ph_def = re.findall('"def":([^"]*),', split_line)[0:2]
            if len(ph_def) == 1:
                ph_def.append(31)
            sp_atk = re.findall('"spa":([^"]*),', split_line)[0:2]
            if len(sp_atk) == 1:
                sp_atk.append(31)
            sp_def = re.findall('"spd":([^"]*),', split_line)[0:2]
            if len(sp_def) == 1:
                sp_def.append(31)
            spe = re.findall('"spe":([^"]*)}', split_line)[0:2]
            if len(spe) == 1:
                spe.append(31)
            natures = "/".join(re.findall('"([^"]*)"', re.findall(r'"natures":\[([^\[]*)]', split_line)[0]))
            moves = re.findall('"move":"([^"]*)"', split_line)[0:4]
            counters = "NA"
            top_mon_sets[mon] = [1, role, items, abilities, teras,
                                 f"{hp[0]}/{ph_atk[0]}/{ph_def[0]}/{sp_atk[0]}/{sp_def[0]}/{spe[0]}", f"{hp[1]}/{ph_atk[1]}/{ph_def[1]}/{sp_atk[1]}/{sp_def[1]}/{spe[1]}",
                                 natures, moves[0], moves[1], moves[2], moves[3], counters]
print("Successfully: Found sets for top used Pokemon")

with open("../data/top-sets.csv", "w") as ts:
    for mon in top_mon_sets:
        ts.write(mon + ",")
        for data in top_mon_sets[mon]:
            if top_mon_sets[mon].index(data) < 12:
                ts.write(f"{data},")
            else:
                ts.write(f"{data}\n")
ts.close()
print("Successfully: Wrote data to top-sets.csv")
