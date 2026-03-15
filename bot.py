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

def get_reddit_meme():
    try:
       
        sub = random.choice(['memes'])
        url = f"https://www.reddit.com/r/{sub}/hot.json?limit=25"
        headers = {"User-Agent": "MyDiscordWebhookBot/1.0"}
        res = requests.get(url, headers=headers).json()
        
        posts = res['data']['children']
        memes = []
        for p in posts:
            data = p['data']
            post_url = data.get('url', '')
            # Check for images, gifs, or reddit videos (v.redd.it)
            if post_url.endswith(('.jpg', '.png', '.gif')) or 'v.redd.it' in post_url:
                # Sending the reddit permalink ensures Discord embeds it correctly
                memes.append(f"https://www.reddit.com{data['permalink']}")
        
        if memes:
            return random.choice(memes)
    except Exception as e:
        print(f"Reddit Error: {e}")
    return None

def get_gif_meme():
    try:
        res = requests.get("https://meme-api.com/gimme").json()
        return res.get('url')
    except Exception as e:
        print(f"GIF Error: {e}")
        return "https://i.imgflip.com/1ur9b0.jpg"

def main():
    chance = random.random()
    
    # 50% YouTube
    if chance < 0.50:
        meme = get_youtube_meme()
    # 40% Reddit (0.50 to 0.90)
    elif chance < 0.90:
        meme = get_reddit_meme()
    # 10% GIFs (0.90 to 1.0)
    else:
        meme = get_gif_meme()
        
    # Fallback just in case a scraper fails
    if not meme:
        meme = get_gif_meme()
        
    print(f"Sending meme: {meme}")
    r = requests.post(WEBHOOK_URL, json={"content": meme})
    print(f"Discord Response: {r.status_code}")

if __name__ == "__main__":
    main()
