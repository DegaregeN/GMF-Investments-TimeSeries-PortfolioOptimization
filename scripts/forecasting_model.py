
import pickle
from statsmodels.tsa.arima.model import ARIMA

def train_arima(train_data):
    model = ARIMA(train_data, order=(5, 1, 0))
    model_fit = model.fit()
    with open('../models/trained_model_arima.pkl', 'wb') as f:
        pickle.dump(model_fit, f)

def main():
    df = pd.read_csv('../data/processed/tsla_data.csv')
    train_data = df['Close'][:int(0.8 * len(df))]
    train_arima(train_data)
