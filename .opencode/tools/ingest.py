import sys
import re
import subprocess
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound


def extract_video_id(url: str) -> str:
    """Extract 11-character YouTube video ID from standard, shortened, or embed URLs."""
    parsed_url = urlparse(url)
    if parsed_url.hostname in ("www.youtube.com", "youtube.com"):
        if parsed_url.path == "/watch":
            return parse_qs(parsed_url.query).get("v", [""])[0]
        if parsed_url.path.startswith(("/embed/", "/v/")):
            return parsed_url.path.split("/")[2]
    elif parsed_url.hostname == "youtu.be":
        return parsed_url.path.lstrip("/")
    
    # Fallback regex match for raw 11-char ID
    match = re.search(r"([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    
    raise ValueError(f"Could not extract a valid YouTube video ID from URL: {url}")


def ingest_youtube(url: str, extract_frames: bool = False) -> str:
    video_id = extract_video_id(url)
    
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        raw_text = " ".join([item["text"] for item in transcript_list])
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        raw_text = f"[TRANSCRIPT UNAVAILABLE: {e}]"

    if extract_frames:
        # Resolve stream URL securely using list argument form (prevents shell injection)
        try:
            stream_url = subprocess.check_output(
                ["yt-dlp", "-g", f"https://www.youtube.com/watch?v={video_id}"],
                text=True
            ).splitlines()[0]

            # Extract 1 frame every 30 seconds via FFmpeg
            ffmpeg_cmd = [
                "ffmpeg",
                "-y",
                "-i", stream_url,
                "-vf", "fps=1/30",
                "frame_%03d.png"
            ]
            subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except (subprocess.CalledProcessError, FileNotFoundError, IndexError) as e:
            sys.stderr.write(f"Frame extraction failed: {e}\n")

    return raw_text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <youtube_url> [--visual]")
        sys.exit(1)

    target_url = sys.argv[1]
    is_visual = "--visual" in sys.argv
    print(ingest_youtube(target_url, extract_frames=is_visual))