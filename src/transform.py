import os
import pandas as pd

os.makedirs("data/transformed", exist_ok=True)

df = pd.read_csv("data/clean/events.csv")

df["date"] = pd.to_datetime(df["timestamp"]).dt.date.astype(str)

df.to_csv("data/transformed/events.csv", index=False)
