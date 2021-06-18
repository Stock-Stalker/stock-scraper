<!-- logo -->
<p align="center">
  <img width="300" src="logo.png">
</p>

<!-- short description -->
<h3 align="center">The stock scrapper behind StockStalker</h3>
<h1 align="center">StockStalker - Stock Scraper</h1>

<p align="center">
    <!-- license -->
    <img src="https://img.shields.io/github/license/Stock-Stalker/stock-scraper" />
    <!-- code size  -->
    <img src="https://img.shields.io/github/languages/code-size/Stock-Stalker/stock-scraper" />
    <!-- issues -->
    <img src="https://img.shields.io/github/issues/Stock-Stalker/stock-scraper" />
    <!-- pull requests -->
    <img src="https://img.shields.io/github/issues-pr/Stock-Stalker/stock-scraper" />
    <!-- number of commits per year -->
    <img src="https://img.shields.io/github/commit-activity/y/Stock-Stalker/stock-scraper" />
    <!-- last commit -->
    <img src="https://img.shields.io/github/last-commit/Stock-Stalker/stock-scraper" />
    <!-- website status -->
    <img src="https://img.shields.io/website?url=https%3A%2F%2Fstockstalker.tk" />
</p>

### Important Files & Folders

The structure of **Stock Scraper** is intented to be fairly straightforward. If you clone this repository in order to run the scripts:

```zsh
git clone https://github.com/Stock-Stalker/stock-scraper
```

You'll have access to two main sub folders:

`data` and `scripts`

As the names suggest, data should be written to the `data` folder, and `scripts` should be run from the `scripts` folder.

### Data

While you're welcome to write new data to the `data` folder, there are a few existing files already which you can use to run the scripts.

`djia_news.csv` contains scraped and labeled headlines for the top thirty companies on the Dow Jones Industrial Average index. This is a portion of the full dataset used to train the initial StockStalker algorithm, available in full on [Kaggle](https://www.kaggle.com/sidarcidiacono/news-sentiment-analysis-for-stock-data-by-company). This file contains nearly 2500 data points.

`dow.csv` contains ticker symbols and full company names of the top 30 Dow Jones Industrial Average index companies.

`nasdaqlisted.csv` contains ticker symbols and full company names of the nearly 3,000 NASDAQ index companies.

`nasdaq_news.csv` contains scraped and labeled headlines for the nearly 3,000 NASDAW index companies. This is the other (larger) portion of the full dataset available on [Kaggle](https://www.kaggle.com/sidarcidiacono/news-sentiment-analysis-for-stock-data-by-company) (also linked above). This file contains about 13,400 data points.

### Scripts

Right now, the script that we've made available to easily call is the `get_data` script. All other functions are easily callable with minimal adjustments. The purpose of this service is largely for us to obtain training data, so minimal effort was put into making any of the other scraping functions flexible and callable on their own (although, it would take an extraordinarily minimal amount of work to adjust this to your need).

In order to call `get_data`, first you'll want to open the `scripts` folder, and take a look at the function call at the bottom of `get_data.py`. Ensure that the filepath being passed into the function call is the correct file that you'd like to write. Please also check out the `get_data()` function and ensure that you're reading from the .csv file that you'd like to be reading from.

Once you ensure that all settings are to your liking, you can run the following from terminal:

If you aren't already in the StockScraper directory:

```zsh
cd stock-scraper
```

Then,

```zsh
python3 -m scripts.get_data
```

As this runs, anytime it enters its `except` block, it will print a count of errors encountered in the format:

```zsh
DataError: 19
```

The `news_fetchers` utils that `get_data()` is dependent on will also print a message when they encounter an except block. In this way, you're able to see output that allows you to anticipate your eventual output in a somewhat rudimentary way, and execution of the script will not stop because the functions encounter empty strings or bad inputs.

Once again, this could be easily manipulated into a slightly easier-to-configure CLI tool if you'd like.
