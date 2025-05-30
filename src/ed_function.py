"""
Modular EDA functions for Financial News Analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer


def load_data(filepath):
    """
    Loads a CSV file into a pandas DataFrame.

    Parameters:
        file_path (str): The path to the file to be loaded.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(filepath)


def add_headline_length(df, headline_col="headline"):
    """Add a column for headline length."""
    df = df.copy()
    df["headline_length"] = df[headline_col].str.len()
    return df


def describe_headline_length(df):
    """Return descriptive statistics for headline length."""
    return df["headline_length"].describe()


def count_articles_per_publisher(df, publisher_col="publisher"):
    """Return article counts per publisher."""
    return df[publisher_col].value_counts()


def plot_articles_per_day(df, date_col="date"):
    """Plot number of articles per day, handling tz-aware and tz-naive values."""
    df = df.copy()
    # Convert to datetime with errors='coerce' to avoid ValueError
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    # Normalize all datetimes to be tz-naive (remove timezone info)
    if hasattr(df[date_col], 'dt'):
        df[date_col] = df[date_col].dt.tz_localize(None)
    daily_counts = df[date_col].dt.date.value_counts().sort_index()
    plt.figure(figsize=(10,4))
    daily_counts.plot()
    plt.title("Articles per Day")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def extract_top_keywords(df, text_col="headline", n_keywords=20):
    """Extract top keywords from text column."""
    vectorizer = CountVectorizer(stop_words="english", max_features=n_keywords)
    X = vectorizer.fit_transform(df[text_col].fillna(""))
    return vectorizer.get_feature_names_out()


