# StockStalker - Predictor API

### Important Files & Folders

The structure of **Stock-Scraper** is intented to be fairly straightforward. If you clone this repository in order to run the scripts:

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



## Makefile Commands

`stop`: Stop the running server

`rm`: Remove all unused containers

`rm-all`: Stop and remove all containers

`rmi`: Remove stockstalker images without removing base images. Useful for speeding up build time when switching from one start script to another such as `make start` to `make test`

`rmi-all`: Remove all images

`purge`: _Use with caution_ Completely purge Docker containers, networks, images, volumes, and cache

`lint`: Run flake8

`build`: Build development server without running the server

`start`: Start development server at port `8080`

`reload`: Stop development server and restart the server at port `8080`

`debug`: Start development server in debug mode

`test`: Start test server

`test-security`: Test security vulnerabilities (must have [snyk](https://support.snyk.io/hc/en-us/articles/360003812538-Install-the-Snyk-CLI) installed globally)

`test-image-security`: Test security vulnerabilities for base images (must have [snyk](https://support.snyk.io/hc/en-us/articles/360003812538-Install-the-Snyk-CLI) installed globally)

`reload-test`: Reload test server

`hard-reload-test`: Remove container, rebuild container, and start test server

## How to Run

To run the app you will need:

- [Docker](https://docs.docker.com/get-docker/)
- [docker-compse](https://docs.docker.com/compose/install/)

The `.env` file is not pushed to GitHub. You'll need to create the file in the root of the `predictor` directory. And within the `.env` file, you'll need:

- API_KEY
- TWITTER_BEARER_TOKEN

Additionally you'll need to create `secrets.mk`, a Makefile at the root of the project with the following vars:

- snyk_auth_token

Once you have your environment fully set up and secrets secured, run:

```bash
make start
```

To stop the app press `CNTRL + C`. Then run:

```bash
make stop
```
