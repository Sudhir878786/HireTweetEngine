from job_scrapers.linkedin_scraper import LinkedInScraper
# from job_scrapers.naukri_scraper import NaukriScraper
from twitter_bot import TwitterBot
from utils import clean_job_description

def fetch_and_post_jobs():
    linkedin_scraper = LinkedInScraper()
    # naukri_scraper = NaukriScraper()

    jobs = linkedin_scraper.fetch_jobs() 
    twitter_bot = TwitterBot()

    for job in jobs:
        job['description'] = clean_job_description(job['description'])
        twitter_bot.post_job(job)

if __name__ == "__main__":
    fetch_and_post_jobs()
