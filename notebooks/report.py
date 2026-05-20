import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("# Event Duration Report")
    return


@app.cell
def __():
    import pandas as pd
    import matplotlib.pyplot as plt

    return pd, plt


@app.cell
def __(pd):
    df = pd.read_csv("data/features/events.csv")
    df
    return (df,)


@app.cell
def __(df, plt):
    plt.figure(figsize=(10, 5))
    plt.hist(df["duration_minutes"], bins=50, edgecolor="black", alpha=0.7)
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Event Durations")
    plt.grid(axis="y", alpha=0.3)
    plt.gca()
    return


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
