import requests
import logging
import time
from src.config import Config

class LinkedInScraper:
    
    def fetch_jobs(self):
        """Fetch jobs from LinkedIn via Apify API."""
        try:
            response = requests.get(f"{self.api_url}?token={self.token}")
            response.raise_for_status()
            jobs = response.json()
            logging.info(f"✅ Fetched {len(jobs)} jobs from LinkedIn.")
            return jobs
        except Exception as e:
            logging.error(f"❌ Error fetching LinkedIn jobs: {e}")
            return []

    def save_jobs_to_json(self, jobs, filename="linkedin_jobs.json"):
        """Save fetched LinkedIn jobs to a JSON file."""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(jobs, f, indent=4)
            logging.info(f"✅ LinkedIn jobs saved to {filename}")
        except Exception as e:
            logging.error(f"❌ Error saving LinkedIn jobs to JSON: {e}")
