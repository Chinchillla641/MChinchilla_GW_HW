# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:40:33 2019

@author: User
"""

import pandas as pd

file = "D:/Git/MChinchilla_GW_HW/11-ETL_Project/Resources/battle_actors.csv"

actors_df = pd.read_csv(file)

count = actors_df.groupby("isqno")["isqno"].count()
count.describe()

actors_df.sort_values(["isqno", "actor"], ascending = True, inplace = True)

actors_df.reset_index(inplace = True)
actors_clean = actors_df.loc[:, ["isqno", "attacker", "actor"]]

actors_clean["count"] = actors_clean.groupby('isqno').cumcount() + 1

actors_clean = pd.pivot(actors_clean, index = 'isqno', columns = "count", values = ["attacker", "actor"])

actors_clean.to_csv(r"D:\Git\MChinchilla_GW_HW\11-ETL_Project.actors_clean.csv")