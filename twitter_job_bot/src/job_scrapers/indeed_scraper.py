import requests
import logging
import time
from src.config import Config

class IndeedScraper:
    def __init__(self):
        self.api_token = Config.APIFY_API_TOKEN

    def trigger_scraper(self):
        """Triggers the Apify Indeed Scraper API."""
        logging.info("Triggering the Apify Indeed Scraper...")
        response = requests.post(f"{Config.APIFY_RUN_URL}?token={self.api_token}")
        if response.status_code == 201:
            logging.info("Scraper triggered successfully.")
        else:
            logging.error(f"Failed to trigger scraper: {response.text}")

    def fetch_jobs(self):
        """Fetch job listings from Apify dataset output."""
        logging.info("Fetching jobs from Apify Indeed Scraper...")
        time.sleep(10)  # Wait for Apify to process the data
        
        response = requests.get(f"{Config.APIFY_OUTPUT_URL}?token={self.api_token}")
        if response.status_code == 200:
            jobs = response.json()
            logging.info(f"Fetched {len(jobs)} jobs successfully.")
            return jobs
        else:
            logging.error("Failed to fetch job listings.")
            return []
