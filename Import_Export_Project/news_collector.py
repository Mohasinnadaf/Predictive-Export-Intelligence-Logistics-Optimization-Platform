import requests
import pandas as pd
from commodities import commodities
import time


API_KEY="d101119ffcfb4d26b9b2652c7c758f2d"


all_news=[]


for commodity in commodities:


    print("Fetching:",commodity)


    url="https://newsapi.org/v2/everything"


    params={

        "q":commodity,

        "language":"en",

        "sortBy":"publishedAt",

        "pageSize":100,

        "apiKey":API_KEY

    }


    response=requests.get(
        url,
        params=params
    )


    data=response.json()



    if "articles" not in data:
        continue



    for article in data["articles"]:


        all_news.append({

        "commodity":commodity,

        "date":article["publishedAt"],

        "title":article["title"],

        "description":article["description"],

        "source":article["source"]["name"]

        })



    time.sleep(1)



df=pd.DataFrame(all_news)


df.to_csv(
"raw_news.csv",
index=False
)


print(
"Total News:",
len(df)
)