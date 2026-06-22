# AI/ML Series - Episode 3
# Data Cleaning

import pandas as pd

data = {
    "Name": ["Sam", "John", "Alice"],
    "Score": [95, None, 91]
}

df = pd.DataFrame(data)

print(df.fillna(0))