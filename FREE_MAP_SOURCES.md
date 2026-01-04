# Free D&D Map Sources

This document lists high-quality, free D&D battle map sources that you can use in your games.

## 🗺️ Professional Map Repositories

### 1. mbround18 VTT Maps (GitHub)
- **URL**: https://github.com/mbround18/vtt-maps
- **Format**: DD2VTT + PNG images
- **Quality**: Professional DungeonDraft-style maps
- **License**: Creative Commons
- **Features**:
  - Maps in `/maps` folder with DD2VTT files
  - Beach, dungeon, forest, town maps
  - Web viewer available
  - Direct download support

### 2. Dice Grimorium Free Library
- **URL**: https://dicegrimorium.com/free-rpg-map-library/
- **Format**: High-res JPG/PNG
- **Quality**: Professional hand-drawn
- **Features**:
  - Ice caves, swamps, city streets
  - Riverside locations
  - Forest and dungeon maps
  - Grid and gridless versions

### 3. 2-Minute Tabletop (Free Tier)
- **URL**: https://2minutetabletop.com/product-category/free/
- **Format**: PNG with grid
- **Quality**: Artistic, hand-painted
- **Features**:
  - Free pack every month
  - Fantasy and modern settings
  - Token art included

### 4. Forgotten Adventures (Free Assets)
- **URL**: https://www.forgotten-adventures.net/
- **Format**: DungeonDraft assets + maps
- **Quality**: Professional
- **Features**:
  - Free asset packs for DungeonDraft
  - Battle maps library
  - Tokens and props

### 5. /r/battlemaps (Reddit)
- **URL**: https://www.reddit.com/r/battlemaps/
- **Format**: Various (PNG, JPG)
- **Quality**: Community-made, varies
- **Features**:
  - Huge variety
  - Daily new maps
  - Free downloads
  - Filter by theme

### 6. Crosshead Studios
- **URL**: https://crossheadstudios.com/
- **Format**: DungeonDraft assets
- **Quality**: Professional
- **Features**:
  - Ghibli-style pack
  - Free and paid assets
  - Compatible with DungeonDraft

## 📥 How to Use These Maps

### Method 1: Download Directly
1. Visit the source website
2. Download the map image (PNG/JPG)
3. Use in your VTT of choice

### Method 2: Clone Git Repositories
```bash
# Clone mbround18 VTT maps
git clone https://github.com/mbround18/vtt-maps.git
cd vtt-maps/maps

# Maps are in subdirectories with DD2VTT files
```

### Method 3: Use This Repo's Downloader (Coming Soon)
We're building a downloader script to fetch maps from these sources automatically.

## 🎨 Map Formats Explained

### DD2VTT Format
- JSON metadata file
- Contains grid info, walls, lighting
- Import directly into Foundry VTT
- Use with DD Import module

### Standard Image Formats
- PNG/JPG with visible grid
- Typical size: 2800x2100px (40x30 grids at 70px/square)
- Upload to any VTT platform
- Manual grid alignment needed

## 🔍 Finding More Maps

### Search Terms
- "free D&D battle maps"
- "VTT maps creative commons"
- "DungeonDraft maps free"
- "Foundry VTT free maps"

### Communities
- Reddit: /r/battlemaps, /r/dndmaps
- Discord: Foundry VTT community
- Patreon: Many map makers offer free tiers

## ⚖️ Licensing

Always check the license before using maps:
- **Creative Commons (CC)**: Usually free for personal use
- **Attribution Required**: Credit the creator
- **Non-Commercial**: Only for home games, not for sale
- **Patreon Content**: Check creator's terms

## 💡 Tips for Building Your Map Library

1. **Organize by Theme**
   ```
   maps/
   ├── dungeons/
   ├── taverns/
   ├── wilderness/
   ├── towns/
   └── special/
   ```

2. **Keep Metadata**
   - Note the source/creator
   - Save DD2VTT files with images
   - Track grid size (usually 70px/square)

3. **Regular Updates**
   - Subscribe to map creators
   - Check /r/battlemaps weekly
   - Follow map makers on social media

4. **Build Encounter Library**
   - Match maps to common encounters
   - Have variety for random encounters
   - Keep both indoor and outdoor options

## 🚀 Using with This Repo

This repository includes:
- Map generator for basic layouts
- Map viewer for any PNG/DD2VTT files
- Organization tools

You can mix generated maps with downloaded professional maps!

---

**Next Steps**: Check out [map_downloader_script.py](map_downloader_script.py) to automatically fetch maps from these sources.
