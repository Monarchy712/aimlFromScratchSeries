# AI/ML Series - Episode 4
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.hist(df["Weight"])

plt.show()