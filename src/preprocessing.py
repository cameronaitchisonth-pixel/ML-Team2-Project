import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def add_features(df: pd.DataFrame, rolling_window: int = 10):
    """
    Add features for ML: returns, rolling volatility, price/volume features, lags.
    Handles NaN and infinite values, ready for scaling.
    """
    df = df.copy()
    
    # Returns and volatility
    df['Return'] = df['Adj Close'].pct_change()
    df['Volatility'] = df['Return'].rolling(rolling_window).std()

    # Price-based features
    df['High_Low_pct'] = (df['High'] - df['Low']) / df['Close']
    df['Close_Open_pct'] = (df['Close'] - df['Open']) / df['Open']
    df['MA5'] = df['Close'].rolling(5).mean()
    df['MA10'] = df['Close'].rolling(10).mean()

    # Volume-based features
    df['Volume_pct_change'] = df['Volume'].pct_change()
    df['Volume_MA5'] = df['Volume'].rolling(5).mean()

    # Lag features
    df['Return_lag1'] = df['Return'].shift(1)
    df['Return_lag2'] = df['Return'].shift(2)
    df['Volatility_lag1'] = df['Volatility'].shift(1)

    # Replace inf with NaN, then drop NaNs
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Features to scale
    features = [
        'Return', 'High_Low_pct', 'Close_Open_pct', 'MA5', 'MA10',
        'Volume_pct_change', 'Volume_MA5', 'Return_lag1', 'Return_lag2', 'Volatility_lag1'
    ]

    # Scaling
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features].values)

    target_col = 'Volatility'
    return df, features, target_col

