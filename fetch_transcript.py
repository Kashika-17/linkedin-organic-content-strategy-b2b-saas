import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SUPADATA_API_KEY")

if not API_KEY:
    print("❌ API key not found in .env")
    exit()

expert = input("Expert name (example: dave-gerhardt): ").strip().lower()

video_url = input("Paste YouTube URL: ").strip()

headers = {
    "x-api-key": API_KEY
}

params = {
    "url": video_url
}

print("\nFetching transcript...\n")

response = requests.get(
    "https://api.supadata.ai/v1/youtube/transcript",
    headers=headers,
    params=params
)

print("Status:", response.status_code)

if response.status_code != 200:
    print(response.text)
    exit()

data = response.json()

transcript = data.get("transcript", "")

folder = "research/youtube-transcripts"

os.makedirs(folder, exist_ok=True)

filename = os.path.join(folder, f"{expert}.md")

with open(filename, "w", encoding="utf-8") as f:
    f.write(transcript)

print(f"\n✅ Transcript saved to:\n{filename}")