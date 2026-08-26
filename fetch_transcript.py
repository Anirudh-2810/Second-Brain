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

            # Extract text from XML using regex (more robust)
            text_matches = re.findall(r'<text start="([^"]+)" dur="([^"]+)">([^<]*)</text>', cap_resp.text)

            transcript = []
            for start_str, dur_str, text in text_matches:
                start = float(start_str)
                # Fix HTML entities - use unicode escapes
                text = text.replace('\u0026amp;', '&').replace('\u0026lt;', '<').replace('\u0026gt;', '>').replace('\u0026quot;', '"').replace('\u0026#39;', "'")
                transcript.append('{:.1f}s: {}'.format(start, text))

            # Save full transcript
            with open('transcript.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(transcript))

            print('Total entries:', len(transcript))
            for line in transcript[:50]:
                print(line)
            print('...')
            break