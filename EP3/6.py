# AI/ML Series - Episode 3
# Aggregation

import pandas as pd

df = pd.read_csv("data.csv")

print("Average Weight:", df["Weight"].mean())
print("Highest Height:", df["Height"].max())