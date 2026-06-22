# AI/ML Series - Episode 3
# Sorting

import pandas as pd

df = pd.read_csv("data.csv")

print(df.sort_values("Weight", ascending=False))