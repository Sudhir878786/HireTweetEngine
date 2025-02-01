# Twitter Job Bot

A simple Python bot that fetches job listings from multiple job boards and posts them on Twitter.

## Features:
- Fetch jobs from **Indeed**, **LinkedIn**, **ZipRecruiter**, **Glassdoor**, and **Google**.
- Save job listings to a **CSV** file.
- Post job listings to **Twitter** in batches.
- Logs actions and errors for transparency.

## Requirements:
- Python 3.x
- `tweepy` for Twitter API integration
- `jobspy` for scraping job listings
- `csv` for saving jobs in CSV format
- `logging` for logging bot activities

## Usage

To run the bot:

```bash
python -m src.twitter_bot