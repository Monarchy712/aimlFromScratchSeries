# AI/ML Series - Episode 3
# Filtering

import pandas as pd

df = pd.read_csv("data.csv")

print(df[df["Height"] >1])