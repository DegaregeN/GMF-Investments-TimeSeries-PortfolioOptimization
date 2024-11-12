
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    df.fillna(method='ffill', inplace=True)
    df = df.set_index('Date')
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[['Open', 'High', 'Low', 'Close', 'Volume']])
    df[['Open', 'High', 'Low', 'Close', 'Volume']] = scaled_data
    return df
