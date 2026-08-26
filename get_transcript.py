from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()
transcript = api.fetch('_OdqYVCTUqs', languages=['en'])
for entry in transcript[:20]:
    print(f'{entry.start:.1f}s: {entry.text}')
print('...')
print(f'Total entries: {len(transcript)}')

# Save full transcript
with open('transcript.txt', 'w', encoding='utf-8') as f:
    for entry in transcript:
        f.write(f'{entry.start:.1f}s: {entry.text}\n')