"""Utility functions to assist our web scraping scripts with dates, formatting, etc."""

import datetime as dt
import time
import requests
from fuzzywuzzy import process

# -------------------------------#
#        Helper Functions        #
# -------------------------------#


def to_epoch(str_time):
    """Take in string time(yyyy-mm-dd) and convert to epoch time."""
    return int(dt.datetime.strptime(str_time, "%Y-%m-%d").timestamp())


def get_today_epoch():
    """Return epoch time of today's date."""
    today = dt.datetime.combine(dt.date.today(), dt.datetime.min.time())
    epoch_today_gmt = int(today.timestamp())
    return epoch_today_gmt


def get_last_weekday_epoch(epochtime):
    """Return the previous workday's date in epoch time."""
    epochtime = dt.datetime.fromtimestamp(epochtime)
    offset = max(1, (epochtime.weekday() + 6) % 7 - 3)
    timedelta = dt.timedelta(offset)
    most_recent = epochtime - timedelta
    most_recent = int(most_recent.timestamp()) - (60 * 60 * 24)
    return most_recent


def get_ticker_from_name(abbr_or_name):
    """
    Return market ticker abbreviation for given company name.

    Input: company name OR abbreviation:string
    Output: dict including symbol, name, and date accessed
    """
    r = requests.get("https://api.iextrading.com/1.0/ref-data/symbols")
    stockList = r.json()
    # Then, if we want the symbol, we can access "symbol" key.
    # If we want name, we extract "name" key.
    return process.extractOne(abbr_or_name, stockList)[0]
