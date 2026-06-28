# import pandas as pd
# import joblib


# model = joblib.load(
#     "commodity_xgboost.pkl"
# )


# def predict_price(data):

#     df = pd.DataFrame([data])


#     prediction = model.predict(
#         df
#     )


#     return prediction[0]




import pandas as pd
import joblib


model = joblib.load(
    "commodity_xgboost.pkl"
)


# Features used while training XGBoost
FEATURES = [
    'total_news',
    'average_sentiment',
    'positive_news',
    'negative_news',
    'neutral_news',
    'news_growth',
    'price',
    'price_change',
    'price_pct_change',
    'MA7',
    'MA30'
]


def predict_price(data):

    # create dataframe
    df = pd.DataFrame([data])


    # keep only training features
    df = df[FEATURES]


    prediction = model.predict(
        df
    )


    return float(prediction[0])