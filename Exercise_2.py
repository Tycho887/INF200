# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:34:12 2023

@author: Michael
"""


# %% Section 1: Counting votes

import pandas as pd
import numpy as np

def table(rows=-1,file="data/2021-09-14_party distribution_1_st_2021.csv"):

    # read data, obly keep relevant columns
    parties = pd.read_csv(file,
                          sep=";",
                          encoding="utf-8",
                          usecols=["Fylkenavn",
                                   "Partikode", 
                                   "Antall stemmer totalt"])
    
    # group by party code, sum votes and drop county names
    parties = parties.groupby(["Partikode"]).sum().drop(columns=["Fylkenavn"])
    # If you are in python 3.8 or earlier, delete the .drop() method

    # rename columns
    parties.rename(columns={"Antall stemmer totalt":"Votes"},inplace=True)

    # calculate percentages
    votes = parties["Votes"].to_numpy()
    percentages = np.round(100*votes/np.sum(votes),2) # round vector to 2 decimals
    
    # create new coloumns
    parties["percentages"] = percentages
    parties["Above 4%"] = percentages>4 # column of booleans

    # Make sure variable rows has a valid value
    if rows not in range(len(parties)): rows=len(parties)
    
    # print sorted table with given number of rows
    print(parties.sort_values(by=["Votes"], ascending=False).iloc[0:rows])
    
# print table with 4, 7 and all rows
table(4); table(7); table()

# %% Section 2: Regex
import re

sentences =["AliA and Per and friends.",
            "Kari and Joe know each other.",
            "James has known Peter since school days."]

def find_pairs(sentence):
    return re.findall(r"\b[A-Z]\w*", sentence)
    # \b matches word boundary, in this case the beginning of a word
    # [A-Z] matches any capital letter
    # \w* matches any number of word characters, lower or upper case.
    # the pattern is thus: any word starting with a capital letter 
    # followed any number of characters, except spaces.

print(f"{'Friendships':^25}\n{'-'*25}")	
for sentence in sentences:
    left, right = find_pairs(sentence)
    # We can do this because we assume there will only be two names in each sentence
    print(f"{left:>11} - {right:<11}")
