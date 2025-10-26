from src.data_loading import load_csv
from src.preprocessing import add_features

# Load raw data
df = load_csv("SPX.csv")

# Preprocess
df_prepared, feature_cols, target_col = add_features(df)

X = df_prepared[feature_cols]
y = df_prepared[target_col]

print(X.head(), y.head())

