import urllib.request
import re
import random
import requests
import os

WEBHOOK_URL = os.environ.get('https://discord.com/api/webhooks/1482843854549024798/_YHgjGH11nvT5IYTJEpmNAx4MVpvIofN8BVEjcpBPpqzN3mnPPv-JHb1qpOHQ8015hvF')

def get_youtube_meme():
    url = "https://www.youtube.com/results?search_query=funny+memes+shorts"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode()
        video_ids = re.findall(r"watch\?v=(\S{11})", html)
        if video_ids:
            # Returns a direct link to a random video from the search
            return f"https://www.youtube.com/watch?v={random.choice(video_ids)}"
    except Exception:
        pass
    return None

def get_gif_meme():
    try:
        res = requests.get("https://meme-api.com/gimme").json()
        return res.get('url')
    except Exception:
        return "https://i.imgflip.com/1ur9b0.jpg" # Fallback meme

def main():
    if random.random() < 0.75:
        meme = get_youtube_meme()
        if not meme: # If YouTube fails, fallback to GIF
            meme = get_gif_meme()
    else:
        meme = get_gif_meme()
        
    requests.post(WEBHOOK_URL, json={"content": meme})

if __name__ == "__main__":
    main()