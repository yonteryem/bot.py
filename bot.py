import requests
import random
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1482843854549024798/_YHgjGH11nvT5IYTJEpmNAx4MVpvIofN8BVEjcpBPpqzN3mnPPv-JHb1qpOHQ8015hvF"

SUBREDDITS = [
    'memes', 'dankmemes', 'FunnyandSad', 'wholesomememes', 
    'PrequelMemes', 'terriblefacebookmemes', 'ProgrammerHumor',
    'humor', 'funny', 'me_irl', 'HistoryMemes', 'BikiniBottomTwitter'
]

def get_meme(subreddit):
    # This API bypasses Reddit's block on GitHub servers
    url = f"https://meme-api.com/gimme/{subreddit}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Failsafe: Make sure it has an image URL
            if data.get('url'):
                return data
    except Exception as e:
        print(f"Error: {e}")
    return None

def main():
    selected_subs = random.sample(SUBREDDITS, 3)
    
    for sub in selected_subs:
        meme = get_meme(sub)
        if meme:
            # Matches your exact requested format
            payload = {
                "content": f"**{meme['title']}** (from r/{sub})\n{meme['url']}"
            }
            requests.post(WEBHOOK_URL, json=payload)
            time.sleep(2)

if __name__ == "__main__":
    main()
