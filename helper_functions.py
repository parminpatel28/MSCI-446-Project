import pandas as pd

def save_df(df: pd.DataFrame, name: str) -> None:
    """
    Save a newly-created DF to the correct path. Returns None.
    Params: 
    - df: pd.DataFrame
    - name: str
    """
    df.to_csv(f"csvs/{name}")

def get_master_df() -> pd.DataFrame:
    """
    Get the most up-to-date master DF. Returns a DF.
    """
    return pd.read_csv("csvs/master_df.csv")