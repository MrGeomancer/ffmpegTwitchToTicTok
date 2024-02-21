import requests

headers = {
    'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    'Referer': 'https://www.twitch.tv/',
    'Origin': 'https://www.twitch.tv',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static.twitchcdn.net/assets/features.clips.components.featured-clips.components.feature-clip-button-dc5f7775af7220bff5a8.css',
    headers=headers,
)

print(response)
