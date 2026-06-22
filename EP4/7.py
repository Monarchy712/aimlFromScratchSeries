# AI/ML Series - Episode 4
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.scatter(df["Weight"], df["Height"])

plt.xlabel("Weight")
plt.ylabel("Height")

plt.show()