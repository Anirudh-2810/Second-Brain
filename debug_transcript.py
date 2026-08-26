import requests
import re
import json

video_id = '_OdqYVCTUqs'
url = 'https://www.youtube.com/watch?v=' + video_id
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
resp = requests.get(url, headers=headers, timeout=10)

# Extract caption tracks
caption_match = re.search(r'"captionTracks":(\[.*?\])', resp.text)
if caption_match:
    captions = json.loads(caption_match.group(1))
    for cap in captions:
        lang = cap.get('languageCode')
        name = cap.get('name', {}).get('simpleText', '')
        print('Language:', lang, 'Name:', name)
        if lang in ['en', 'en-orig', 'en-US']:
            cap_url = cap['baseUrl']
            cap_resp = requests.get(cap_url, headers=headers, timeout=10)
            
            # Print first 5000 chars to see structure
            print('First 5000 chars of transcript XML:')
            print(cap_resp.text[:5000])
            break