from helpers.helpers import get_channel_subscribers, get_total_views_from_datetime
from datetime import datetime, timedelta

one_week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%SZ')
one_month_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ')


channel_id = "UCvCTWHCbBC0b9UIeLeNs8ug"

def main():
    get_channel_subscribers(api_key, channel_id)
    get_total_views_from_datetime(api_key, channel_id, one_month_ago)
    
if __name__ == "__main__":
    main()
