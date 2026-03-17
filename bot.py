import requests
import random
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1482843854549024798/_YHgjGH11nvT5IYTJEpmNAx4MVpvIofN8BVEjcpBPpqzN3mnPPv-JHb1qpOHQ8015hvF"

SUBREDDITS = [
    'dankmemes', 'shitposting', 'HolUp', 'ImFinnaGoToHell', 'cursedcomments',
    'okbuddyretard', 'SipsTea', 'Unexpected', 'dank_meme', 'meme', 'Discordmemes',
    '2meirl4meirl', 'me_irl', 'memes', 'PerfectlyCutBooms', 'perfectlycutscreams',
    'hmm', 'hmmm', 'blursedimages', 'cursedimages', 'meirl', 'wtf',
    'watchpeopledieinside', 'youseeingthisshit', 'nonononoyes', 'yesyesyesno',
    'maybemaybemaybe', 'madlads', '2mad4madlads', 'insanepeoplefacebook',
    'crackheadcraigslist', 'comedyheaven', 'comedynecromancy', 'bonehurtingjuice',
    'antimeme', 'technicallythetruth', 'greentext', '4chan', 'greentexts',
    'fakehistoryporn', 'bertstrips', 'surrealmemes', 'deepfriedmemes', 'nukedmemes',
    'moldymemes', 'terriblefacebookmemes', 'ihadastroke', 'engrish', 'boneappletea',
    'skamtebord', 'softwaregore', 'oldpeoplefacebook', 'youngpeopleyoutube',
    'rareinsults', 'clevercomebacks', 'murderedbywords', 'suicidebywords',
    'kamikazebywords', 'wellthatsucks', 'crappyoffbrands', 'awfuleverything',
    'atbge', 'diwhy', 'redneckengineering', 'idiotsincars', 'tooktoomuch',
    'imthemaincharacter', 'donthelpjustfilm', 'kidsarefuckingstupid', 'whenthe',
    'wordington', 'dramatictext', 'shitpostcrusaders', 'BikiniBottomTwitter',
    'TrollCoping', 'depression_memes', 'darkhumor', 'HistoryMemes', 'PrequelMemes', 
    'LotRMemes', 'raimimemes', 'NolanBatmanMemes', 'marvelmemes', 'gamingmemes', 
    'LeagueOfMemes', 'ValorantMemes', 'MinecraftMemes', 'Overwatch_Memes',
    'ProgrammerHumor', 'mathmemes', 'dndmemes', 'Grimdank', 'PoliticalCompassMemes',
    'facepalm', 'absoluteunits', 'tifu', 'mildlyinfuriating', 'ContagiousLaughter',
    'ComedyCemetery', 'ComedyHell', 'ihavesex', 'iamverybadass', 'iamverysmart'
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
    target_count = random.randint(3, 6)
    sent_count = 0

    available_subs = random.sample(SUBREDDITS, len(SUBREDDITS))
    
    for sub in available_subs:
        if sent_count >= target_count:
            break
            
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
