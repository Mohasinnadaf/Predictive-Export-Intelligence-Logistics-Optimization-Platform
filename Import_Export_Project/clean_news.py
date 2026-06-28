import pandas as pd


df=pd.read_csv(
"raw_news.csv"
)



# remove empty rows

df.dropna(
subset=[
"title",
"description"
],
inplace=True
)



df["date"]=pd.to_datetime(
df["date"]
)



# combine text

df["text"]=(
df["title"]
+
" "
+
df["description"]
)



# remove duplicate news

df.drop_duplicates(
subset="text",
inplace=True
)



df.to_csv(
"clean_news.csv",
index=False
)


print(df.head())
