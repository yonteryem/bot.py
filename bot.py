import requests
import random
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1482843854549024798/_YHgjGH11nvT5IYTJEpmNAx4MVpvIofN8BVEjcpBPpqzN3mnPPv-JHb1qpOHQ8015hvF"

SUBREDDITS = [
    'memes', 'dankmemes', 'FunnyandSad', 'wholesomememes', 
    'PrequelMemes', 'terriblefacebookmemes', 'ProgrammerHumor',
    'humor', 'funny', 'me_irl', 'HistoryMemes', 'BikiniBottomTwitter'
]

def get_reddit_meme(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=50"
    # A unique User-Agent is CRITICAL to avoid 429 errors
    headers = {"User-Agent": "h3llwalker-meme-fetcher-v1.2"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Error {response.status_code} fetching r/{subreddit}")
            return None
            
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        valid_memes = []
        for p in posts:
            post = p['data']
            if post.get('stickied') or post.get('over_18'):
                continue
                
            img_url = post.get('url', '')
            if any(img_url.lower().endswith(ext) for ext in ['.jpg', '.png', '.gif', '.jpeg']):
                valid_memes.append({
                    "url": img_url,
                    "title": post.get('title', 'Meme'),
                    "permalink": f"https://reddit.com{post.get('permalink')}"
                })
        
        return random.choice(valid_memes) if valid_memes else None
    except Exception as e:
        print(f"Failed to scrape r/{subreddit}: {e}")
        return None

def main():
    selected_subs = random.sample(SUBREDDITS, 3)
    print(f"Checking subreddits: {', '.join(selected_subs)}")

    for sub in selected_subs:
        meme = get_reddit_meme(sub)
        if meme:
            print(f"Posting: {meme['title']}")
            payload = {
                "content": f"**{meme['title']}** (from r/{sub})\n{meme['url']}"
            }
            requests.post(WEBHOOK_URL, json=payload)
            time.sleep(2) # Avoid spamming Discord too fast
        else:
            print(f"No image found in r/{sub}")

if __name__ == "__main__":
    main()
