# Map Downloader Guide

## Quick Start

Run the interactive downloader:
```bash
python map_downloader_script.py
```

## Download Options

### Option 1: Sample Maps (Recommended for First Time)
- Downloads **2 maps from each category**
- Quick way to see variety
- ~26 maps total
- **Best for**: Testing, getting a preview

### Option 2: Specific Categories
- Choose categories you need
- Downloads ALL maps from selected categories
- **Best for**: Themed campaigns

Available categories:
- `beach` - Coastal and shore maps
- `dungeons` - Underground complexes
- `forest` - Woodland encounters
- `taverns` - Inns and drinking establishments
- `locations` - Various buildings and sites
- `encounters` - Combat-ready battle maps
- `travel` - Roads and paths
- `desert` - Arid environments
- `tundra` - Frozen landscapes
- `cyberpunk` - Futuristic urban
- `base_building` - Structures and facilities
- `spires` - Towers and tall structures
- `other` - Miscellaneous maps

### Option 3: Download Everything
- Downloads **ALL** maps from repository
- 100+ professional maps
- **Warning**: May take 10-20 minutes
- **Best for**: Building complete library

### Option 4: Single Map
- Download one specific map
- You need to know:
  - Category name (e.g., "beach")
  - Map name (e.g., "simple-beach")
- **Best for**: Targeted downloads

## What Gets Downloaded

For each map, you'll get:
- ✅ **`.dd2vtt` file** - Main map file with embedded image + metadata
- ✅ **`.md` file** - Description and details (if available)

## File Organization

Maps are organized by category:
```
maps/
├── beach/
│   ├── simple-beach.dd2vtt
│   ├── simple-beach.md
│   └── ...
├── dungeons/
│   ├── underground-complex.dd2vtt
│   └── ...
├── taverns/
│   └── ...
└── index.json  (created after download)
```

## Using Downloaded Maps

### In Foundry VTT
1. Install the **DD Import** module: https://foundryvtt.com/packages/dd-import/
2. Drag and drop `.dd2vtt` files into your game
3. Map imports automatically with walls and grid!

### In Roll20/Fantasy Grounds
1. You'll need to extract PNG images from `.dd2vtt` files
2. DD2VTT files are JSON with base64-encoded images
3. Or use a converter tool

### Reading Map Details
- Open `.md` files in any text editor
- Contains map descriptions, dimensions, and usage tips

## Tips

### Fast Preview
Use Option 1 to quickly see what's available before committing to larger downloads.

### Bandwidth Friendly
Script includes small delays between downloads to be respectful to GitHub's servers.

### Resuming Downloads
If interrupted, just run again - it won't re-download existing files.

### Finding Specific Maps
Browse the repo first: https://github.com/mbround18/vtt-maps/tree/main/maps

## Troubleshooting

### "Failed to access category"
- Check internet connection
- GitHub API may be rate-limited (wait a few minutes)

### "Failed to download"
- Map file may have been moved/renamed
- Check if map exists in repo

### Empty download
- Verify category name spelling
- Some categories may have submaps in subdirectories

## Examples

### Example 1: Get Tavern Maps
```bash
python map_downloader_script.py
# Choose option 2
# Enter: 4  (taverns is 4th in the list)
```

### Example 2: One Specific Map
```bash
python map_downloader_script.py
# Choose option 4
# Category: beach
# Map name: simple-beach
```

## Advanced: Manual Download

If you prefer manual control:

```python
from map_downloader_script import MapDownloader

downloader = MapDownloader()

# Download specific map
downloader.download_map_from_category('beach', 'simple-beach')

# Download all from a category
downloader.discover_and_download_category('dungeons')

# Download with limit
downloader.discover_and_download_category('forest', limit=5)
```

## Credit

All maps from: **mbround18/vtt-maps**
- GitHub: https://github.com/mbround18/vtt-maps
- License: Creative Commons
- Support the creator: https://ko-fi.com/mbround18
