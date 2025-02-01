import tweepy
import logging
import csv
from jobspy import scrape_jobs
from src.config import Config

class TwitterBot:
    def __init__(self):
        """Initialize Twitter API using OAuth 2.0 with tweepy.Client"""
        try:
            # OAuth 2.0 with tweepy.Client
            self.client = tweepy.Client(
                consumer_key=Config.TWITTER_API_KEY,
                consumer_secret=Config.TWITTER_API_SECRET,
                access_token=Config.TWITTER_ACCESS_TOKEN,
                access_token_secret=Config.TWITTER_ACCESS_SECRET
            )
            logging.info("✅ Twitter Authentication Successful")
        except tweepy.errors.Unauthorized as e:
            logging.error(f"❌ Twitter Authentication Failed: {e}")
            exit()
        except Exception as e:
            logging.error(f"❌ Error during TwitterBot Initialization: {e}")
            exit()

    def post_job(self, job):
        """Post a job to Twitter."""
        tweet = f"🚀 New Job Alert 🚀\n\n" \
                f"🔹 {job.get('title', 'N/A')}\n" \
                f"📍 Location: {job.get('location', 'N/A')}\n" \
                f"💰 Salary: {job.get('salary', 'N/A')}\n" \
                f"🔗 Apply Here: {job.get('job_url', 'N/A')}\n\n" \
                f"#Hiring #SoftwareJobs #TechJobs"

        try:
            if self.client:
                self.client.create_tweet(text=tweet)
                logging.info("✅ Tweet posted successfully.")
            else:
                logging.error("❌ API client not found.")
        except tweepy.errors.TweepyException as e:
            logging.error(f"❌ Error posting tweet: {e}")

    def save_jobs_to_csv(self, jobs, filename="jobs.csv"):
        """Save fetched jobs to a CSV file."""
        try:
            jobs.to_csv(filename, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
            logging.info(f"✅ Jobs saved to {filename}")
        except Exception as e:
            logging.error(f"❌ Error saving jobs to CSV: {e}")

    def fetch_jobs(self):
        """Fetch jobs using jobspy."""
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google"],
            search_term="software engineer",
            google_search_term="software engineer jobs near San Francisco, CA since yesterday",
            location="San Francisco, CA",
            results_wanted=20,
            hours_old=72,
            country_indeed='USA'
        )
        return jobs

    def run(self):
        """Fetch jobs, save them to CSV, and post them on Twitter."""
        jobs = self.fetch_jobs()
        if jobs.empty:
            logging.info("⚠️ No jobs to post.")
            return
        
        # Save jobs to a CSV file
        self.save_jobs_to_csv(jobs)

        # Post top 5 jobs on Twitter
        for _, job in jobs.head(1).iterrows():
            self.post_job(job)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="logs/bot.log", filemode="a",
                        format="%(asctime)s - %(levelname)s - %(message)s")
    bot = TwitterBot()
    bot.run()
