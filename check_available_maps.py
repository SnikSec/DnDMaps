from map_downloader_script import MapDownloader
import requests

downloader = MapDownloader()
total = 0

print("Maps available per category:")
print("=" * 40)

for cat in downloader.categories:
    try:
        response = requests.get(f"{downloader.github_api_base}/{cat}")
        contents = response.json()
        dd2vtt_files = [x for x in contents if x.get("type") == "file" and x["name"].endswith(".dd2vtt")]
        count = len(dd2vtt_files)
        total += count
        if count > 0:
            print(f"  {cat:20} {count:3} maps")
    except Exception as e:
        print(f"  {cat:20} Error: {e}")

print("=" * 40)
print(f"Total available: {total} maps")
