"""
Quantitative analysis functions for Task 2: Stock price analysis using TA-Lib and PyNance
"""
import pandas as pd
import matplotlib.pyplot as plt

class QuantAnalysis:
    @staticmethod
    def load_stock_data(filepath):
        """Load stock price data with OHLCV columns."""
        try:
            df = pd.read_csv(filepath)
            required_cols = {"Open", "High", "Low", "Close", "Volume"}
            if not required_cols.issubset(df.columns):
                raise ValueError(f"Missing columns: {required_cols - set(df.columns)}")
            return df
        except Exception as e:
            print(f"Error loading stock data: {e}")
            return None