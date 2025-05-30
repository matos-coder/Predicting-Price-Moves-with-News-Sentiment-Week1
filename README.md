# Predicting-Price-Moves-with-News-Sentiment-Week1

A Python-based data analysis project focusing on extracting insights from financial news headlines through exploratory data analysis, text processing, and visualization.

📁 Overview
This project combines advanced data handling and analysis techniques to explore and uncover patterns in financial news data. The suite is designed to process raw news datasets and derive meaningful insights using Python, ensuring modular and extensible code for various use cases.

Key Features:

Descriptive Statistics: Analyze headline lengths and publication trends.
Topic Modeling: Extract common keywords and significant phrases using NLP.
Time Series Analysis: Examine publication frequency trends over time.
Publisher Analysis: Identify and compare publishers' contributions and trends.

✨ Features
📰 Financial News Analysis

Data Loading:

Load financial news data from ../data/raw/raw_analyst_ratings.csv.

Preview and clean the data for analysis.

Descriptive Statistics:

Compute headline length statistics (mean, median, min, max).

Count articles per publisher.

Publishing Trends:

Analyze article publication patterns over time.

Identify spikes or trends related to specific events.

Text Analysis:

Extract top keywords and common phrases using NLP.

Perform domain-level analysis of publisher contributions.

Visualizations:

Publication trends by date and day of the week.

Weekly and daily article counts.

Keyword and publisher domain analysis.

📂 Dataset Description
News Headlines Dataset

Location: ../data/raw/raw_analyst_ratings.csv

Columns:

Unnamed: 0: Index

headline: News title

url: Article link

publisher: Source of the article

date: Publication datetime

stock: Ticker symbol associated with the news

🧰 Dependencies
Install the required packages:

bash
Copy
Edit
pip install requirment.txt

🧑‍💻 Usage
1. Clone the Repository:

git clone https://github.com/matos-coder/Predicting-Price-Moves-with-News-Sentiment-Week1
cd Predicting-Price-Moves-with-News-Sentiment-Week1

2. Install Dependencies:

pip install -r requirements.txt

3. Run the Analysis:
Execute the main script or run specific analyses:

python main_analysis.py

4. Visualizations:
Output charts and analysis results will be saved to the results/ directory.

📌 Example Outputs
Headline Statistics:

Mean Length: 75.5 characters

Max Length: 512 characters

Top Publication Day:

March 12, 2020: 1,866 articles published

Keyword Extraction:

Top terms include: "FDA approval," "price target," "market crash."

🧪 Customization
Want to adapt this project for a different dataset or analysis goal?

Replace the news dataset file in ../data/raw/ (ensure the structure matches).

Update the relevant column names in the configuration.

🤝 Contributing
Pull requests are welcome! If you'd like to contribute to this project:

Fork the repository.

Create a new feature branch.

Submit a pull request for review.

For major changes, open an issue to discuss your ideas first.

📬 Contact
For questions, feedback, or collaboration:

Email: matiasashenafi0@gmail.com