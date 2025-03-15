from helpers.helpers import get_channel_subscribers, get_total_views_from_datetime, get_channel_name
from datetime import datetime, timedelta
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
X_API_KEY = os.getenv("X_API_KEY")
X_API_KEY_SECRET = os.getenv("X_API_KEY_SECRET")
X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

one_week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")
one_month_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

# YouTube channel ID
channel_id = "UCvCTWHCbBC0b9UIeLeNs8ug"


def setup_twitter_client():
    """Set up and return an authenticated Twitter client using tweepy."""
    try:
        # Initialize the client with authentication tokens
        client = tweepy.Client(
            bearer_token=X_BEARER_TOKEN,
            consumer_key=X_API_KEY,
            consumer_secret=X_API_KEY_SECRET,
            access_token=X_ACCESS_TOKEN,
            access_token_secret=X_ACCESS_TOKEN_SECRET,
        )
        return client
    except Exception as e:
        print(f"Error setting up Twitter client: {e}")
        return None


def main():
    try:

        twitter_client = setup_twitter_client()
        
        name = get_channel_name(YOUTUBE_API_KEY, channel_id)
        subscribers = get_channel_subscribers(YOUTUBE_API_KEY, channel_id)
        views_week = get_total_views_from_datetime(YOUTUBE_API_KEY, channel_id, one_week_ago)
        views_month = get_total_views_from_datetime(YOUTUBE_API_KEY, channel_id, one_month_ago)
        
        
        print(f'Channel {name}')
        print(f'Subs {subscribers}')
        print(f'Views last week {views_week}')
        print(f'Views last month {views_month}')

    except Exception as e:
        print(f"Error in main function: {e}")
        return


if __name__ == "__main__":
    main()
