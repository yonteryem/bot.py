import requests
import random

WEBHOOK_URL = "https://discord.com/api/webhooks/1482843854549024798/_YHgjGH11nvT5IYTJEpmNAx4MVpvIofN8BVEjcpBPpqzN3mnPPv-JHb1qpOHQ8015hvF"

SUBREDDITS = [
    'memes', 'dankmemes', 'FunnyandSad', 'wholesomememes', 
    'PrequelMemes', 'terriblefacebookmemes', 'ComedyCemetery', 
    'AdviceAnimals', 'MemeEconomy', 'ProgrammerHumor',
    'darkhumourmemes', 'DarkHumorAndMemes', 'blackhumor',
    'humor', 'funny', 'me_irl', '2meirl4meirl', 
    'HistoryMemes', 'BikiniBottomTwitter', 'surrealmemes'
]

def get_reddit_meme(subreddit):
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=30"
        headers = {"User-Agent": "MyDiscordWebhookBot/2.0"}
        res = requests.get(url, headers=headers).json()
        
        posts = res['data']['children']
        valid_memes = []
        
        for p in posts:
            data = p['data']
            if data.get('stickied'):
                continue
                
            post_url = data.get('url', '')
            # Filter for images/gifs
            if any(post_url.endswith(ext) for ext in ['.jpg', '.png', '.gif', '.jpeg']):
                valid_memes.append(f"https://www.reddit.com{data['permalink']}")
        
        if valid_memes:
            return random.choice(valid_memes)
    except Exception as e:
        print(f"Error fetching from r/{subreddit}: {e}")
    return None

def main():
    num_to_select = random.randint(3, len(SUBREDDITS) // 2)
    selected_subs = random.sample(SUBREDDITS, num_to_select)
    
    print(f"Selecting {num_to_select} subreddits...")

    for sub in selected_subs:
        meme_link = get_reddit_meme(sub)
        if meme_link:
            print(f"Posting from r/{sub}: {meme_link}")
            payload = {"content": f"**From r/{sub}:**\n{meme_link}"}
            requests.post(WEBHOOK_URL, json=payload)
        else:
            print(f"Skipping r/{sub} (no suitable meme found).")

if __name__ == "__main__":
    main()
