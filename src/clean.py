import os
import pandas as pd
from dateutil import parser

VALID_EVENT_TYPES = {"click", "scroll", "view", "login", "purchase"}

os.makedirs("data/clean", exist_ok=True)

df = pd.read_csv("data/raw/events.csv", dtype=str)

df.dropna(inplace=True)

df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
df.dropna(subset=["duration_seconds"], inplace=True)
df = df[df["duration_seconds"] > 0]

df = df[df["event_type"].str.lower().isin(VALID_EVENT_TYPES)]
df["event_type"] = df["event_type"].str.lower()


def normalize_ts(ts):
    dt = parser.parse(ts)
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


df["timestamp"] = df["timestamp"].apply(normalize_ts)

df.to_csv("data/clean/events.csv", index=False)
