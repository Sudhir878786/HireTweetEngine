import os
import logging
import time
from metathreads import MetaThreads
from jobspy import scrape_jobs
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(level=logging.INFO)

# MetaThreads setup
class ThreadsBot:
    def __init__(self):
        """Initialize MetaThreads using login credentials from environment variables"""
        self.threads = MetaThreads()
        self.threads.login(os.getenv('THREADS_USERNAME'), os.getenv('THREADS_PASSWORD'))
        logging.info("✅ MetaThreads Authentication Successful")

    def post_job(self, job):
        """Post a job on MetaThreads"""
        job_caption = f"🚀 **Job Opportunity**: {job['title']}\n" \
                      f"🏢 **Company**: {job['company']}\n" \
                      f"📍 **Location**: {job['location']}\n" \
                      f"🔗 **Apply Here**: {job['job_url']}\n" \
                      f"\n#JobOpportunity #Hiring #Careers #TechJobs"

        try:
            # Posting the job to thread
            self.threads.post_thread(thread_caption=job_caption)
            logging.info(f"✅ Successfully posted job: {job['title']}")
        except Exception as e:
            logging.error(f"❌ Error posting job: {job['title']}. Retrying in 15 seconds...")
            time.sleep(15)
            self.post_job(job)

    def run(self):
        """Fetch jobs and post them one by one"""
        # Fetch jobs from multiple sites
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google"],
            search_term="software engineer",
            google_search_term="software engineer jobs near San Francisco, CA since yesterday",
            location="San Francisco, CA",  # Added India location
            results_wanted=5,  # Fetch multiple jobs
            hours_old=72,
            country_indeed='USA',
        )

        logging.info(f"✅ Jobs fetched: {len(jobs)}")
        logging.info(f"Fetched Jobs Structure:\n{jobs.head()}")

        if len(jobs) > 0:
            # Post only the first job
            job = jobs.iloc[0]  # Get the first job from the list
            self.post_job(job)
        else:
            logging.info("No jobs found.")

if __name__ == "__main__":
    bot = ThreadsBot()
    bot.run()
