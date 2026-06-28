import pandas as pd



df=pd.read_csv(
"news_with_sentiment.csv"
)



df["date"]=pd.to_datetime(
df["date"]
)



# create time features

df["year"]=df.date.dt.year

df["month"]=df.date.dt.month




final=df.groupby(
[
"commodity",
"year",
"month"
]
).agg(

total_news=
("title","count"),


average_sentiment=
("sentiment_score","mean"),



positive_news=
(
"sentiment_score",
lambda x:(x==1).sum()
),


negative_news=
(
"sentiment_score",
lambda x:(x==-1).sum()
),


neutral_news=
(
"sentiment_score",
lambda x:(x==0).sum()
)


).reset_index()



final.to_csv(
"commodity_news_dataset.csv",
index=False
)



print(final.head())




final["news_growth"]=(
final.groupby("commodity")
["total_news"]
.pct_change()
)


final.fillna(
0,
inplace=True
)


final.to_csv(
"final_export_news_dataset.csv",
index=False
)