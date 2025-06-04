# Quantitative Analysis – Financial Data (Task 2)

This folder contains the quantitative analysis notebook and supporting code for Task 2: Stock price analysis using TA-Lib and PyNance.

## Objective

Load, analyze, and visualize stock price data using technical indicators and financial metrics. The goal is to apply quantitative finance techniques to understand price movements and trends, leveraging both TA-Lib and PyNance.

## Workflow Overview

The workflow is divided into several key stages, implemented in [`notebooks/quantitative analysis.ipynb`](notebooks/quantitative analysis.ipynb):

### 1. Data Loading & Preparation

- **Load historical stock price data** (e.g., for AAPL) from CSV using the `QuantAnalysis` class.
- Ensure the dataset contains the required columns: `Open`, `High`, `Low`, `Close`, and `Volume`.
- Handle missing or malformed data as needed.

### 2. Technical Indicator Calculation (TA-Lib)

- **Simple Moving Average (SMA):** Calculate the 20-day SMA to smooth price trends.
- **Relative Strength Index (RSI):** Compute the 14-day RSI to identify overbought/oversold conditions.
- **MACD:** Generate MACD, Signal, and Histogram values to analyze momentum and trend changes.

### 3. Financial Metrics with PyNance

- Fetch additional financial metrics for the selected ticker and date range using PyNance.
- Integrate these metrics for deeper quantitative analysis.

### 4. Visualization

- Visualize the Close price alongside SMA, RSI, and MACD using Matplotlib.
- Use plots to interpret indicator signals and price action.

## Notebook Structure

The main workflow is implemented in [`quantitative analysis.ipynb`](notebooks/quantitative%20analysis.ipynb):

1. **Import Libraries & Setup**
   - Import pandas, TA-Lib, PyNance, and the custom `QuantAnalysis` class.
2. **Load Data**
   - Load stock price data from `../data/yfinance_data/AAPL_historical_data.csv`.
3. **Calculate Indicators**
   - Apply TA-Lib functions for SMA, RSI, and MACD.
4. **Fetch Financial Metrics**
   - Use PyNance to retrieve additional metrics for the ticker.
5. **Visualization**
   - Plot Close price, SMA, RSI, and MACD for analysis.

## Key Performance Indicators (KPIs)

- **Proactivity to Self-Learn:** References to external documentation and tutorials are provided.
- **Accuracy of Indicators:** Calculations use industry-standard libraries (TA-Lib, PyNance).
- **Completeness of Data Analysis:** The workflow covers data loading, indicator calculation, metric fetching, and visualization.

## Example Outputs

- DataFrame with Close, SMA, RSI, MACD, and related columns.
- Plots showing price trends, momentum, and indicator signals.
- Printed financial metrics from PyNance.

## References

- [TA-Lib Documentation](https://mrjbq7.github.io/ta-lib/)
- [PyNance Documentation](https://pynance.readthedocs.io/en/latest/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Python for Finance Tutorial (Kaggle)](https://www.kaggle.com/code/mmmarchetti/tutorial-python-for-finance)
- [YouTube: Python for Finance](https://www.youtube.com/watch?v=5cZJPvEYRbA)

## Customization

- To analyze a different stock, replace the CSV file path or ticker symbol in the notebook.
- Ensure your data includes the required OHLCV columns.
- Adjust indicator parameters as needed for your analysis.

## Contact

For questions or collaboration, contact: matiasashenafi0@gmail.com