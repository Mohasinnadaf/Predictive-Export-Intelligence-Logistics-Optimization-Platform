import pandas as pd
import numpy as np

from commodities import commodities



# -----------------------------
# Load sentiment dataset
# -----------------------------

df = pd.read_csv(
    "news_sentiment.csv"
)



# -----------------------------
# Date processing
# -----------------------------

df["date"] = pd.to_datetime(
    df["date"]
)


df["year"] = df["date"].dt.year

df["month"] = df["date"].dt.month



# -----------------------------
# Create monthly summary
# -----------------------------

summary = df.groupby(
    [
        "commodity",
        "year",
        "month"
    ]
).agg(

    total_news =
    ("title","count"),


    average_sentiment =
    ("sentiment","mean"),


    positive_news =
    (
        "sentiment",
        lambda x:(x==1).sum()
    ),


    negative_news =
    (
        "sentiment",
        lambda x:(x==-1).sum()
    ),


    neutral_news =
    (
        "sentiment",
        lambda x:(x==0).sum()
    )

).reset_index()



# -----------------------------
# Create all commodity-month rows
# -----------------------------

months = df[
    [
        "year",
        "month"
    ]
].drop_duplicates()



all_rows=[]



for commodity in commodities:

    for _,row in months.iterrows():

        all_rows.append(
            {

            "commodity":commodity,

            "year":row["year"],

            "month":row["month"]

            }
        )



complete = pd.DataFrame(
    all_rows
)



# -----------------------------
# Merge with summary
# -----------------------------

final = complete.merge(
    summary,
    how="left",
    on=[
        "commodity",
        "year",
        "month"
    ]
)



# missing news = 0

final.fillna(
    0,
    inplace=True
)



# -----------------------------
# Sort data
# -----------------------------

final = final.sort_values(
    [
        "commodity",
        "year",
        "month"
    ]
)



# -----------------------------
# Calculate safe news growth
# -----------------------------


final["previous_news"] = (

    final.groupby("commodity")
    ["total_news"]
    .shift(1)

)



# avoid divide by zero

final["previous_news"] = (
    final["previous_news"]
    .replace(0,1)
)



final["news_growth"] = (

    (final["total_news"] -
     final["previous_news"])
    /
    final["previous_news"]

)



# remove infinity

final["news_growth"] = (
    final["news_growth"]
    .replace(
        [np.inf,-np.inf],
        0
    )
)



final["news_growth"] = (
    final["news_growth"]
    .fillna(0)
)



# -----------------------------
# Remove helper column
# -----------------------------

final.drop(
    columns=[
        "previous_news"
    ],
    inplace=True
)



# -----------------------------
# Save final dataset
# -----------------------------

final.to_csv(
    "commodity_news_dataset_90.csv",
    index=False
)



print(
    final.head(30)
)


print(
    "Shape:",
    final.shape
)