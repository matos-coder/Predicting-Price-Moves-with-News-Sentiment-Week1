"""
Quantitative analysis functions for Task 2: Stock price analysis using TA-Lib and PyNance
"""
import pandas as pd
import matplotlib.pyplot as plt
import talib
import yfinance as yf
import pynance as pn
from textblob import TextBlob
import os
import traceback

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
    @staticmethod
    def calculate_technical_indicators(df):
        """Calculate SMA, RSI, and MACD using TA-Lib."""
        try:
            df = df.copy()
            df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
            df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)
            macd, macdsignal, macdhist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
            df['MACD'] = macd
            df['MACD_signal'] = macdsignal
            df['MACD_hist'] = macdhist
            return df
        except Exception as e:
            print(f"Error calculating technical indicators: {e}")
            return df

    @staticmethod
    def plot_technical_indicators(df, ticker="Stock"):
        """Visualize Close price, SMA, RSI, and MACD."""
        try:
            fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
            # Price and SMA
            axes[0].plot(df['Close'], label='Close')
            axes[0].plot(df['SMA_20'], label='SMA 20')
            axes[0].set_title(f'{ticker} Close Price & SMA')
            axes[0].legend()
            # RSI
            axes[1].plot(df['RSI_14'], label='RSI 14', color='orange')
            axes[1].axhline(70, color='red', linestyle='--', alpha=0.5)
            axes[1].axhline(30, color='green', linestyle='--', alpha=0.5)
            axes[1].set_title('RSI 14')
            axes[1].legend()
            # MACD
            axes[2].plot(df['MACD'], label='MACD')
            axes[2].plot(df['MACD_signal'], label='Signal')
            axes[2].bar(df.index, df['MACD_hist'], label='Hist', color='gray', alpha=0.3)
            axes[2].set_title('MACD')
            axes[2].legend()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting technical indicators: {e}")

    @staticmethod
    def get_pynance_metrics(ticker, start, end):
        """Fetch financial metrics using PyNance."""
        try:
            data = pn.data.history(ticker, start, end)
            return data
        except Exception as e:
            print(f"Error fetching data from PyNance: {e}")
            return None

    @staticmethod
    def get_financial_metrics(ticker, start, end):
        """Fetch financial metrics using yfinance."""
        try:
            # Create ticker object
            stock = yf.Ticker(ticker)
            
            # Fetch historical data
            data = stock.history(start=start, end=end)
            
            if data.empty:
                print(f"No data found for ticker {ticker}")
                return None
                
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
        


class NewsSentimentCorrelation:
    """
    Task 3: Correlation between News Sentiment and Stock Movement
    Functions for aligning news and stock data, performing sentiment analysis, calculating returns, and correlation analysis.
    """
    @staticmethod
    def load_and_align_data(news_path, stock_path):
        """
        Loads news and stock data, parses dates, and aligns both datasets by date.
        Handles mixed timezone data and invalid entries.
        
        Returns:
            tuple: (news_df, stock_df) - Both are DataFrames or both are None
        """
        try:
            # Validate file paths first
            if not os.path.exists(news_path):
                raise FileNotFoundError(f"News file not found: {news_path}")
            if not os.path.exists(stock_path):
                raise FileNotFoundError(f"Stock file not found: {stock_path}")

            # Load datasets with explicit datetime parsing
            news_df = pd.read_csv(
                news_path,
                parse_dates=['date'],
                dayfirst=True,
                on_bad_lines='warn',
                encoding_errors='replace'
            )
            
            stock_df = pd.read_csv(
                stock_path,
                parse_dates=['Date'],
                dayfirst=True,
                on_bad_lines='warn',
                encoding_errors='replace'
            )

            # Check required columns
            if 'date' not in news_df.columns:
                raise ValueError("News data missing 'date' column")
            if 'Date' not in stock_df.columns:
                raise ValueError("Stock data missing 'Date' column")

            # Clean data
            news_df = news_df.dropna(subset=['date'])
            stock_df = stock_df.dropna(subset=['Date'])

            # Handle timezones - convert all to naive datetime
            news_df['date'] = pd.to_datetime(news_df['date'], utc=True).dt.tz_localize(None).dt.date
            stock_df['date'] = pd.to_datetime(stock_df['Date'], utc=True).dt.tz_localize(None).dt.date

            # Validate
            if news_df.empty:
                raise ValueError("News DataFrame is empty after cleaning")
            if stock_df.empty:
                raise ValueError("Stock DataFrame is empty after cleaning")

            print("News data sample:")
            print(news_df[['date', 'headline']].head())
            print("\nStock data sample:")
            print(stock_df[['date', 'Close']].head())

            return news_df, stock_df

        except Exception as e:
            print(f"\nERROR in load_and_align_data: {str(e)}\n")
            print(f"News path: {news_path}")
            print(f"Stock path: {stock_path}")
            traceback.print_exc()
            return None, None



    @staticmethod
    def compute_sentiment(news_df):
        """
        Adds a 'sentiment' column to news_df using TextBlob polarity.
        """
        news_df['sentiment'] = news_df['headline'].astype(str).apply(lambda x: TextBlob(x).sentiment.polarity)
        return news_df

    @staticmethod
    def compute_daily_returns(stock_df):
        """
        Computes daily percentage returns from closing prices.
        """
        stock_df = stock_df.copy()
        stock_df['daily_return'] = stock_df['Close'].pct_change()
        return stock_df[['date', 'daily_return']].dropna()

    @staticmethod
    def aggregate_daily_sentiment(news_df):
        """
        Aggregates sentiment scores by date (mean if multiple headlines per day).
        """
        daily_sentiment = news_df.groupby('date')['sentiment'].mean().reset_index()
        daily_sentiment.rename(columns={'sentiment': 'avg_sentiment'}, inplace=True)
        return daily_sentiment

    @staticmethod
    def merge_and_correlate(daily_sentiment, daily_returns):
        """
        Merges daily sentiment and returns by date and computes Pearson correlation.
        """
        merged = pd.merge(daily_sentiment, daily_returns, on='date', how='inner')
        correlation = merged['avg_sentiment'].corr(merged['daily_return'])
        return merged, correlation