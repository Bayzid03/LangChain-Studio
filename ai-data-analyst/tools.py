from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from langchain.tools import Tool

# Load CSV data
data = pd.read_csv("data/sales.csv", parse_dates=["date"])

# Query data using a pandas expression
def query_data(expression: str):
    """Return datetime rows that match a pandas query string"""
    try:
        df = data.query(expression).copy()
        return df.to_dict(orient="records")[:50]
    except Exception as e:
        return f"Query error: {e}"

# Calculate basic statistics
def quick_stats(column: str, metric: str):
    if metric == "sum": val = data[column].sum()
    elif metric == "avg": val = data[column].mean()
    else: return "Metric must be 'sum' or 'avg'"
    return {metric: val}

# Plot timeseries data
def plot_timeseries(column: str):
    plt.figure()
    data.groupby("date")[column].sum().plot()
    
    charts_dir = Path("charts")
    charts_dir.mkdir(exist_ok=True)
    
    fname = charts_dir / f"{column}_{datetime.now():%Y%m%d_%H%M%S}.png"
    plt.title(column + " overtime")
    plt.savefig(fname)
    plt.close()
    
    return str(fname)

# Save logs to a uniquely named file
def save_log(text: str):
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    fname = logs_dir / f"{datetime.now():%Y%m%d_%H%M%S}.txt"
    fname.write_text(text)
    
    return str(fname)
