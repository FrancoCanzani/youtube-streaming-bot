import requests
from datetime import datetime, timedelta

one_week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%SZ')
one_month_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ')

def get_channel_subscribers(api_key, channel_id):
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "snippet,contentDetails,statistics",
        "id": channel_id,
        "key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("items")[0].get("snippet").get("subscriberCount")

    else:
        print(f"Request failed with status code: {response.status_code}")


def get_channel_name(api_key, channel_id):
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "snippet,contentDetails,statistics",
        "id": channel_id,
        "key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("items")[0].get("snippet").get("title")

    else:
        print(f"Request failed with status code: {response.status_code}")


def get_videos_from_datetime(api_key, channel_id, datetime):
    
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "channelId": channel_id,
        "order": "date",
        "maxResults": 50,  
        "type": "video",
        "publishedAfter": datetime,  
        "key": api_key
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        videos = []
        for item in data.get("items", []):
            statistics = get_video_statistics(api_key, item["id"]["videoId"])
            
            video = {
                "title": item["snippet"]["title"],
                "videoId": item["id"]["videoId"],
                "publishedAt": item["snippet"]["publishedAt"],
                "viewCount": statistics["viewCount"] if statistics else "N/A",
                "commentCount": statistics["commentCount"] if statistics else "N/A",
            }
            
            videos.append(video)
        
        return videos
    else:
        print(f"Request failed with status code: {response.status_code}")
        return []
    
def get_total_views_from_datetime(api_key, channel_id, datetime):
    videos = get_videos_from_datetime(api_key, channel_id, datetime)
    
    total = 0
    
    for video in videos:
        total += int(video["viewCount"])
    
    print(total)
    
def get_video_statistics(api_key, video_id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "statistics,snippet",
        "id": video_id,
        "key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json().get("items")[0].get("statistics")
        return data
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.json())
        return []