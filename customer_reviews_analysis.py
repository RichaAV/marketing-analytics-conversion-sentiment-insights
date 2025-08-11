
import pandas as pd
import pyodbc

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.width', 0)        # Auto-adjust width
nltk.download('vader_lexicon')

# Function to fetch data from SQL database
def fetch_data():
    conn_str = (
        "Driver={SQL Server Native Client RDA 11.0};"
        "Server=LAPTOP-C8UGB811;"
        "Database=marketing_analytics;"
         "Trusted_Connection=yes;" 
    )

    # Establish connection to the database
    conn = pyodbc.connect(conn_str)

    # SQL query to fetch customer_reviews data
    query = "SELECT * FROM customer_reviews"

    # Execute the query and store data in the dataframe
    df = pd.read_sql(query, conn)

    #Close the connection
    conn.close()

    return df

# Calling the function fetch_data 
customer_reviews_df = fetch_data()

# Initialising SentimentIntensityAnalyzer
sa = SentimentIntensityAnalyzer()

# Function to calculate sentiment scores
def calculate_sentiment_scores(review):
    # Assign sentiment score
    sentiment = sa.polarity_scores(review)

    # Return the compound score, which is a normalized score between -1 (most negative) and 1 (most positive)
    return sentiment['compound']


# Function to categorize sentiment using both the sentiment score and the review rating
def categorize_sentiment(score, rating):
    if score > 0.05:  # Positive sentiment score
        if rating >= 4:
            return 'Positive'  # High rating and positive sentiment
        elif rating == 3:
            return 'Mixed Positive'  # Neutral rating but positive sentiment
        else:
            return 'Mixed Negative'  # Low rating but positive sentiment
    elif score < -0.05:  # Negative sentiment score
        if rating <= 2:
            return 'Negative'  # Low rating and negative sentiment
        elif rating == 3:
            return 'Mixed Negative'  # Neutral rating but negative sentiment
        else:
            return 'Mixed Positive'  # High rating but negative sentiment
    else:  # Neutral sentiment score
        if rating >= 4:
            return 'Positive'  # High rating with neutral sentiment
        elif rating <= 2:
            return 'Negative'  # Low rating with neutral sentiment
        else:
            return 'Neutral'  # Neutral rating and neutral sentiment

# Define a function to bucket sentiment scores into text ranges
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'  # Strongly positive sentiment
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'  # Mildly positive sentiment
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'  # Mildly negative sentiment
    else:
        return '-1.0 to -0.5'  # Strongly negative sentiment

# Applying sentiment analysis to calculate sentiment scores for each review
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment_scores)

# Apply sentiment categorization using both text and rating
customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)

# Apply sentiment bucketing to categorize scores into defined ranges
customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

# Display the first few rows of the DataFrame with sentiment scores, categories, and buckets
print(customer_reviews_df.head())

# Save the DataFrame with sentiment scores, categories, and buckets to a new CSV file
customer_reviews_df.to_csv(r'C:\Users\Richa\Documents\My Learning\Analytics\Marketing_Analytics\fact_customer_reviews_with_sentiment.csv', index=False)
print("saved")