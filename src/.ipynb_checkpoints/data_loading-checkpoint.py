import pandas as pd
from pathlib import Path

def load_csv(file_name: str) -> pd.DataFrame:
    """
    Load a CSV file from the data directory.
    """
    data_path = Path(__file__).parent.parent / "data" / file_name 
    if not data_path.exists():
        raise FileNotFoundError(f"{data_path} not found.")

    df = pd.read_csv(data_path, parse_dates=['Date'])
    df = df.sort_values('Date').reset_index(drop=True)
    return df 
