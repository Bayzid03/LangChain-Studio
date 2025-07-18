import pandas as pd, os, datetime, matplotlib.pyplot as plt
from langchain.tools import Tool

data = pd.read_csv("data/sales.csv",parse_dates=["date"])

def query_data(expression:str):
    """Return datetime rows that match a pandas query string"""
    try:
        df=data.query(expression).copy()
        return df.to_dict(orient="records")[:50]
    
    except Exception as e:
        return f"Query error:{e}"
    
def quick_stats(column:str, metric:str):
    if metric=="sum": val = data[column].sum()
    elif metric == "avg": val = data[column].mean()
    else: return "Metric must be 'sum' or 'avg' "
    return {metric:val}