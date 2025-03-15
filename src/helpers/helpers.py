import requests

def get_channel_subscribers(api_key, channel_id):
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "snippet,contentDetails,statistics",
        "id": channel_id,
        "key": api_key,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "items" in data and data["items"]:
            return data["items"][0]["statistics"].get("subscriberCount", "N/A")
        else:
            print("No data found for the given channel ID.")
            return "N/A"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching channel subscribers: {e}")
        return "N/A"

def get_channel_name(api_key, channel_id):
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "snippet,contentDetails,statistics",
        "id": channel_id,
        "key": api_key,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "items" in data and data["items"]:
            return data["items"][0]["snippet"].get("title", "N/A")
        else:
            print("No data found for the given channel ID.")
            return "N/A"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching channel name: {e}")
        return "N/A"

def get_videos_from_datetime(api_key, channel_id, datetime):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "channelId": channel_id,
        "order": "date",
        "maxResults": 50,
        "type": "video",
        "publishedAfter": datetime,
        "key": api_key,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        videos = []
        for item in data.get("items", []):
            video_id = item["id"].get("videoId")
            if not video_id:
                continue
            statistics = get_video_statistics(api_key, video_id)
            video = {
                "title": item["snippet"].get("title", "N/A"),
                "videoId": video_id,
                "publishedAt": item["snippet"].get("publishedAt", "N/A"),
                "viewCount": statistics.get("viewCount", "N/A") if statistics else "N/A",
                "commentCount": statistics.get("commentCount", "N/A") if statistics else "N/A",
            }
            videos.append(video)
        return videos
    except requests.exceptions.RequestException as e:
        print(f"Error fetching videos: {e}")
        return []

def get_total_views_from_datetime(api_key, channel_id, datetime):
    try:
        videos = get_videos_from_datetime(api_key, channel_id, datetime)
        total = 0
        for video in videos:
            try:
                total += int(video["viewCount"])
            except ValueError:
                print(f"Invalid view count for video: {video['title']}")
        return total
    except Exception as e:
        print(f"Error calculating total views: {e}")
        return 0

def get_video_statistics(api_key, video_id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {"part": "statistics,snippet", "id": video_id, "key": api_key}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "items" in data and data["items"]:
            return data["items"][0].get("statistics", {})
        else:
            print(f"No statistics found for video ID: {video_id}")
            return {}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching video statistics: {e}")
        return {}
