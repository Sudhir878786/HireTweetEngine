import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    APIFY_RUN_URL = "https://api.apify.com/v2/actor-runs/Hpv9Cbqi1izyfTH8j"
    APIFY_OUTPUT_URL = "https://api.apify.com/v2/datasets/PfugYYjiWM2WAEgM0/items"
    APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")  # Store API key in .env

    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")



