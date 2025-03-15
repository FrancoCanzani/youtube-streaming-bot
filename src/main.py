from helpers.helpers import (
    get_channel_subscribers,
    get_total_views_from_datetime,
    get_channel_name,
)
from datetime import datetime, timedelta, timezone
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

now = datetime.now(timezone.utc)
one_week_ago = (now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")

# YouTube channel ID
channel_id = "UCvCTWHCbBC0b9UIeLeNs8ug"

# Vorterix, Olga, Luzu, Azz, Blender, La Casa, Bondi, Urbana Play, Carajo, El Observador, Neura, Gelatina, Radio con Vos, Rock & Pop
channels = [
    "UCvCTWHCbBC0b9UIeLeNs8ug",
    "UC7mJ2EDXFomeDIRFu5FtEbA",
    "UCTHaNTsP7hsVgBxARZTuajw",
    "UCgLBmUFPO8JtZ1nPIBQGMlQ",
    "UCSbo4jtRPEK8qu6c04j2dXQ",
    "UCxHSIJgKZ8xVXwLGaGZEmKg",
    "UC4u0BhsSi33PS20_1JHiC5A",
    "UCnZidingmuqNkaT9Wm64Xxg",
    "UCC1kfsMJko54AqxtcFECt-A",
    "UC4mdhKZXjrKoq5aVG6juHEg",
    "UC-rI_XNppHJO-Ga4RW_CDKw",
    "UC-40U87JsevMIMn7PMw4jPw",
    "UCWSfXECGo1qK_H7SXRaUSMg",
    "UCxDteokWBemJvLI_I0VUGdA",
    "UCAlQ5f7mhnkfM6jjXeJDw7g",
]


def setup_twitter_client():
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

        for channel_id in channels:
            name = get_channel_name(YOUTUBE_API_KEY, channel_id)
            subscribers = get_channel_subscribers(YOUTUBE_API_KEY, channel_id)
            views_week = get_total_views_from_datetime(
                YOUTUBE_API_KEY, channel_id, one_week_ago
            )

            print(f"Channel {name}")
            print(f"Subs {subscribers}")
            print(f"Views last week {views_week}")

    except Exception as e:
        print(f"Error in main function: {e}")
        return


if __name__ == "__main__":
    main()
