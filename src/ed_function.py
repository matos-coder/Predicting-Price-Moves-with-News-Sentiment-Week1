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

