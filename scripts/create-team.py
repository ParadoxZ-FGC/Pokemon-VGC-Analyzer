# Create a viable team : Grab Pokemon from highest pick rates, put together combo of 2-3 Support sets, 2-3 Offensive and 1-2 Defensive sets

import re
import os


viable = False
while not viable:
    team = re.split(", ", input("What (viable) Pokemon do you want the team to be centered around? (E.G. 'Archaludon, Cresselia'): ").lower())
    for mon in team:
        m_v = False
        for filename in os.listdir("data/smogon-dumps"):
            if mon in filename:
                m_v = True
        if m_v:
            viable = True
print("Successfully: Gathered viable team core")

# Do Something


