reg = "g"
uniq = []

with open("temp.txt", "w", encoding="utf-8") as temp:
    for line in open(f"reg-{reg}_tourney_urls.txt").readlines():
        s = False
        for u in uniq:
            if line in u:
                s = True
        if s is False:
            temp.write(line)
            uniq.append(line)

with open(f"reg-{reg}_tourney_urls.txt", "w", encoding="utf-8") as new:
    for line in sorted(open("temp.txt").readlines()):
        new.write(line)

clear = open("temp.txt", "w", encoding="utf-8")
