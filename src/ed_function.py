"""
Financial News EDA Functions

This module contains reusable functions for exploratory data analysis of financial news data.
Includes functions for:
- Data loading and cleaning
- Text analysis
- Time series analysis
- Visualization

All functions are designed to be modular and return either DataFrames or visualization objects.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from typing import Optional

def load_data(filepath: str, parse_dates: Optional[list] = None) -> pd.DataFrame:
    """
    Load CSV data with optional date parsing.
    
    Args:
        filepath: Path to CSV file
        parse_dates: List of columns to parse as dates
        
    Returns:
        Loaded DataFrame
    """
    return pd.read_csv(filepath, parse_dates=parse_dates)

def add_headline_length(df: pd.DataFrame, headline_col: str = "headline") -> pd.DataFrame:
    """
    Add headline length column to DataFrame.
    
    Args:
        df: Input DataFrame
        headline_col: Name of column containing headlines
        
    Returns:
        DataFrame with added 'headline_length' column
    """
    df = df.copy()
    df["headline_length"] = df[headline_col].str.len()
    return df

def describe_headline_length(df: pd.DataFrame) -> pd.Series:
    """Return descriptive stats for headline lengths."""
    return df["headline_length"].describe()

def count_articles_per_publisher(df: pd.DataFrame, publisher_col: str = "publisher") -> pd.Series:
    """Count articles by publisher."""
    return df[publisher_col].value_counts()

def parse_date_column(df: pd.DataFrame, date_col: str = "date") -> pd.DataFrame:
    """
    Parse date column and standardize timezone handling.
    
    Args:
        df: Input DataFrame
        date_col: Name of date column
        
    Returns:
        DataFrame with parsed dates
    """
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    if hasattr(df[date_col], 'dt'):
        df[date_col] = df[date_col].dt.tz_localize(None)
    return df

def plot_articles_per_day(df: pd.DataFrame, date_col: str = "date", save_path: Optional[str] = None) -> None:
    """
    Plot daily article counts.
    
    Args:
        df: Input DataFrame
        date_col: Name of date column
        save_path: Optional path to save plot
    """
    df = parse_date_column(df, date_col)
    daily_counts = df[date_col].dt.date.value_counts().sort_index()
    
    plt.figure(figsize=(12, 6))
    daily_counts.plot()
    plt.title("Articles per Day")
    plt.xlabel("Date")
    plt.ylabel("Count")
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

def extract_top_keywords(df: pd.DataFrame, text_col: str = "headline", n_keywords: int = 20) -> list:
    """
    Extract most frequent keywords from text.
    
    Args:
        df: Input DataFrame
        text_col: Name of text column
        n_keywords: Number of keywords to extract
        
    Returns:
        List of top keywords
    """
    vectorizer = CountVectorizer(stop_words="english", max_features=n_keywords)
    X = vectorizer.fit_transform(df[text_col].fillna(""))
    return vectorizer.get_feature_names_out().tolist()

def plot_weekly_article_count(df: pd.DataFrame, date_col: str = "date", save_path: Optional[str] = None) -> None:
    """
    Plot weekly article counts.
    
    Args:
        df: Input DataFrame
        date_col: Name of date column
        save_path: Optional path to save plot
    """
    df = parse_date_column(df, date_col)
    weekly_counts = df.set_index(date_col).resample("W").size()
    
    plt.figure(figsize=(12, 6))
    weekly_counts.plot()
    plt.title("Weekly Article Count")
    plt.xlabel("Week")
    plt.ylabel("Count")
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

def publisher_domain_analysis(df: pd.DataFrame, publisher_col: str = "publisher") -> pd.Series:
    """
    Extract and analyze publisher domains from email addresses.
    
    Args:
        df: Input DataFrame
        publisher_col: Name of publisher column
        
    Returns:
        Value counts of publisher domains
    """
    df = df.copy()
    df["publisher_domain"] = df[publisher_col].str.extract(r'@([\w\.-]+)')
    return df["publisher_domain"].value_counts()