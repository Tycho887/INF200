# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:47:17 2023

@author: Michael
"""


#%% Task 1: A Greeting

#name = input("Please enter your name: ")
#print(f"Welcome to INF201 {name} !")

#%% Task 2: A pretty greeting

# name = input("Please enter your name: ")

# print(f"""
# {"".join(["*" for i in range(0,len(name)+23)])}
# * Welcome to INF201 {name}! *
# {"".join(["*" for i in range(0,len(name)+23)])}
# """)
# %% Task 3: Tabulating data

# print(f"{'-'*20}\n{'x':>6} {'x^2':>6} {'x^3':>6}\n{'-'*20}")
# for i in range(11): print(f"{i:>6} {i**2:>6} {i**3:>6}")
# print(f"{'-'*20}")


# %% Task 4: Read and tabulate data  

with open("data/norway_municipalities_2017.csv", "r", encoding="utf-8") as f:
        districts = {}; f.readline()
        for line in f: 
            municipality, district, population = line.split(",")
            try: districts[district]+=int(population)
            except: districts[district]=int(population) 
print(f"""{'-'*30}\n{'District':<20}{'Population':>10}\n{'-'*30}""")
for district in sorted(list(districts.keys())): print(f"{district:<20}{districts[district]:>10}")
print(f"{'-'*30}")

# Task 5: Read and plot data

import matplotlib.pyplot as plt

plt.bar([i[0:2] for i in districts.keys()],districts.values())
plt.show()
