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
    url = f"https://meme-api.com/gimme/{subreddit}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('url'):
                return data
    except Exception:
        pass
    return None

def main():
    target_count = random.randint(3, 6) # Picks a random number between 3 and 6
    sent_count = 0
    
    while sent_count < target_count:
        sub = random.choice(SUBREDDITS)
        meme = get_meme(sub)
        
        if meme:
            url = meme['url']
            if url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                payload = {"embeds": [{"image": {"url": url}}]}
                response = requests.post(WEBHOOK_URL, json=payload)
                
                if response.status_code == 204:
                    sent_count += 1
                    time.sleep(2)

if __name__ == "__main__":
    main()
