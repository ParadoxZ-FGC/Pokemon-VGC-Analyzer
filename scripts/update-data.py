# Crawl sites : Gather top sets/pick rates

import requests  # library that allows reading web pages

regulation = "f"
root_urls = ["https://victoryroadvgc.com/2024-season-calendar/", "https://www.smogon.com/dex/sv/formats/vgc24-regulation-{}/".format(regulation)]

vr_base = requests.get(root_urls[0])          # Victory Road 2024 Season Calendar page object
smogon_reg_base = requests.get(root_urls[1])  # Smogon current Regulation page object

# search site(s)

# find top ? pokemon and sets

# write pick rates (maybe sets) to file

print(vr_base.text)
