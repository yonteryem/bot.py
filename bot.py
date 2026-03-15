import urllib.request
import re
import random
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1482843854549024798/_YHgjGH11nvT5IYTJEpmNAx4MVpvIofN8BVEjcpBPpqzN3mnPPv-JHb1qpOHQ8015hvF"

def get_youtube_meme():
    try:
        url = "https://www.youtube.com/results?search_query=funny+memes+shorts"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode()
        video_ids = re.findall(r"watch\?v=(\S{11})", html)
        if video_ids:
            return f"https://www.youtube.com/watch?v={random.choice(video_ids)}"
    except Exception as e:
        print(f"YouTube Error: {e}")
    return None

def get_gif_meme():
    try:
        res = requests.get("https://meme-api.com/gimme").json()
        return res.get('url')
    except Exception as e:
        print(f"GIF Error: {e}")
        return "https://i.imgflip.com/1ur9b0.jpg"

def main():
    # 75% Video, 25% GIF
    if random.random() < 0.75:
        meme = get_youtube_meme()
        if not meme:
            meme = get_gif_meme()
    else:
        meme = get_gif_meme()
    
    print(f"Sending meme: {meme}")
    r = requests.post(WEBHOOK_URL, json={"content": meme})
    print(f"Discord Response: {r.status_code}")

if __name__ == "__main__":
    main()
