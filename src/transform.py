import os
import pandas as pd

os.makedirs("data/transform", exist_ok=True)

df = pd.read_csv("data/clean/events.csv")

df["date"] = pd.to_datetime(df["timestamp"]).dt.date.astype(str)

df.to_csv("data/transform/events.csv", index=False)
