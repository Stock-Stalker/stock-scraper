"""Obtain data for model training."""
from scripts.news_fetchers import reddit_worldnews_fetcher, djia_fetcher
import pandas as pd

import csv
import time
from fuzzywuzzy import process

t1 = time.perf_counter()


def preprocess(filepath, col_name):
    """
    Take in a filepath, and returns a clean version of
    column 'companyName'. Since this will be used as
    The search keyword, it's important to cut out words that
    will over-limit search results.

    Input: filepath, relative or absolute. Type:String
           col_name, name of your 'company name' column header for your particular file.
            Type: String
    Output: list of cleaned company names. Type:List of Strings
    """
    # Initialize empty list for companyNames
    names_list = []
    # Read in file using pandas' read_csv() function
    data = pd.read_csv(filepath, header=0, usecols=[1])
    # This isn't the most dynamic replace function, please
    # feel free to update and make more flexible based on your
    # use case.  This will work perfectly with nasdaqlisted.csv if
    # you use our data.
    for name in list(data[col_name]):
        name = name.partition(" - ")[0]
        name = (
            name.replace("[^a-zA-Z]", " ")
            .replace("Inc.", "")
            .replace("Inc", "")
            .replace("Corp", "")
            .replace("Corporation", "")
            .replace("Ltd.", "")
            .replace("Limited", "")
            .strip()
        )
        names_list.append(name)

    return names_list


def get_data(file_to_write):
    """
    Call news_sentiment_analysis in a loop.

    Input: file_to_write -> filepath (abs. or relative).
            Type:String
           slice_from -> if you're appending to an existing file, you can
            begin appending data from this index on.
            Default:0, Type:Integer between 0 and the length of your data
    Output:csv containing labels:
        Ticker:Company name, string
        Headlines: Titles, descriptions, strings
        Sentiment: 0, 1, or 2
    """
    fieldnames = ["Label", "Ticker", "Headline"]
    nasdaq_names = preprocess("data/nasdaqlisted.csv", "companyName")
    counter = 0
    # If you're writing a file for the first time,
    # mode should = "w"
    # Please also uncomment "data_writer.writeheader()" if you want
    # headers on your new csv file
    with open(file_to_write, mode="a") as data:
        data_writer = csv.DictWriter(data, fieldnames=fieldnames)
        # data_writer.writeheader()
        for company_name in nasdaq_names:
            # You're able to change these dates as you see fit, even though they aren't parameterized.
            news = reddit_worldnews_fetcher.top25news(
                "2000-01-01", "2021-03-13", company_name, 25
            )
            try:
                for n in news:
                    # Clean up data a bit
                    headline = n[0].replace(",", "")
                    date = n[1]
                    label = djia_fetcher.get_djia_label(date, company_name)
                    data_writer.writerow(
                        {
                            "Label": label[0],
                            "Ticker": label[1],
                            "Headline": headline,
                        }
                    )
            except TypeError:
                counter += 1
                print("DataError: ", counter)

    return


print("CALLING GET DATA")

if __name__ == "__main__":
    # TODO: pass in your filepath if using a different file!
    get_data("data/nasdaq_news.csv")

t2 = time.perf_counter()
print(f"Finished in {t2 - t1} seconds")
