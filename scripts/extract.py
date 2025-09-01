import pandas as pd

def extract_csv(path):
    return pd.read_csv(path)

def extract_json(path):
    return pd.read_json(path)