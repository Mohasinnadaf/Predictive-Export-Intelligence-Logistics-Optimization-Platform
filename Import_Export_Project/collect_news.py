import requests
import pandas as pd
import time

from commodities import commodities


API_KEY="d101119ffcfb4d26b9b2652c7c758f2d"


data=[]


for c in commodities:

    print("Fetching:",c)

    url="https://newsapi.org/v2/everything"


    params={

        "q":c,

        "language":"en",

        "sortBy":"publishedAt",

        "pageSize":100,

        "apiKey":API_KEY
    }


    r=requests.get(
        url,
        params=params
    )


    result=r.json()


    if "articles" not in result:
        continue



    for a in result["articles"]:

        data.append({

        "commodity":c,

        "date":a["publishedAt"],

        "title":a["title"],

        "description":a["description"]

        })


    time.sleep(1)



df=pd.DataFrame(data)


df.dropna(inplace=True)


df.to_csv(
"raw_news.csv",
index=False
)


print(df.shape)
