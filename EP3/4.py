# AI/ML Series - Episode 3
# Multiple Columns

import pandas as pd

df = pd.read_csv("data.csv")

print(df[["Name", "Weight"]])