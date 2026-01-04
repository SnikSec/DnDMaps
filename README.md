# DnDMaps
Professional D&D battle map collection and download tools for virtual tabletop games

## Overview
A curated resource for **high-quality, free D&D maps** perfect for Dungeon Masters.

This repository provides:
- 📚 **Curated links** to 6+ professional free map sources
- 🔧 **Download tools** to fetch maps from GitHub repositories
- 📖 **Organization guides** for building your map library
- 🎮 **VTT integration** instructions for Foundry, Roll20, Fantasy Grounds

Access **thousands of professional, hand-drawn maps** from talented artists who provide their work for free.

## What You Get

### 🗺️ Professional Map Sources
- **GitHub Repositories** - mbround18/vtt-maps with DungeonDraft-quality maps
- **Dice Grimorium** - Hand-drawn artistic maps (ice caves, swamps, dungeons)
- **2-Minute Tabletop** - Free tier with professional assets
- **/r/battlemaps** - Daily community contributions
- **Forgotten Adventures** - High-quality free assets
- **And more** - See [FREE_MAP_SOURCES.md](FREE_MAP_SOURCES.md) for complete list

### 🔧 Tools Included
- **Map downloader script** - Automated downloading from repos and URLs
- **Comprehensive guides** - How to find, organize, and use maps
- **VTT integration tips** - Foundry VTT, Roll20, Fantasy Grounds
- **Licensing information** - Know what you can use commercially

### ✨ Map Quality
All curated sources provide:
- ✅ Hand-drawn artistic detail
- ✅ Professional textures and lighting
- ✅ High resolution (suitable for VTT and print)
- ✅ Often includes DD2VTT format for Foundry
- ✅ Free for personal use (check individual licenses)

## Getting Started

### Step 1: Browse Map Sources
Read [FREE_MAP_SOURCES.md](FREE_MAP_SOURCES.md) to see all available sources.

### Step 2: Download Maps

**Quick Method - Use the Downloader** (recommended)
```bash
# Clone this repository
git clone https://github.com/SnikSec/DnDMaps.git
cd DnDMaps

# Install Python dependency
pip install -r requirements.txt

# Run interactive downloader
python map_downloader_script.py

# Follow the menu to download maps!
```

See [DOWNLOADER_GUIDE.md](DOWNLOADER_GUIDE.md) for detailed instructions.

**Manual Method - Clone Map Repository**
```bash
# Clone the entire map repository
git clone https://github.com/mbround18/vtt-maps.git
cd vtt-maps/maps

# Maps are ready to use!
```

## Quick Start Examples

### Get Maps from GitHub Repository

**Option 1: Clone the entire repository**
```bash
# Clone mbround18/vtt-maps repository
git clone https://github.com/mbround18/vtt-maps.git
cd vtt-maps/maps

# Maps are ready to use - each folder has DD2VTT files!
```

**Option 2: Use the downloader script**
```bash
# Interactive downloader with menu options
python map_downloader_script.py

# Options:
# 1. Download sample maps (2 per category) - Quick preview
# 2. Download from specific categories - Choose what you need
# 3. Download ALL maps - Complete collection
# 4. Download specific map - Single map download
```

The downloader script will:
- ✅ Fetch maps directly from mbround18/vtt-maps
- ✅ Organize them by category (beach, dungeons, taverns, etc.)
- ✅ Download DD2VTT files ready for Foundry VTT
- ✅ Include description files (.md) when available
- ✅ Create an index.json for easy browsing

### Browse Free Map Libraries
- **Dice Grimorium**: https://dicegrimorium.com/free-rpg-map-library/
- **2-Minute Tabletop**: https://2minutetabletop.com/
- **/r/battlemaps**: https://www.reddit.com/r/battlemaps/


## Using Maps in VTT Platforms

### Foundry VTT (Recommended for DD2VTT files)
1. Install the **DD Import** module from Foundry's module browser
2. Drag and drop `.dd2vtt` files from downloaded maps
3. Map imports automatically with:
   - Correct grid alignment
   - Wall data for line-of-sight
   - Proper dimensions

### Roll20
1. Upload PNG files as maps
2. Set page settings:
   - Grid: Match the map (usually 70 pixels per square)
   - Align grid with map overlay
3. Manually set walls/lighting if needed

### Fantasy Grounds
1. Import PNG as map image
2. Configure grid settings to match map
3. Standard VTT maps use 70 pixels per square

### Tabletop Simulator
1. Upload PNG to image hosting (Imgur, etc.)
2. Use image URL in Tabletop Simulator
3. Scale to match grid

## Organizing Your Map Library

### Recommended Structure
```
maps/
├── dungeons/
│   ├── ice_caves/
│   ├── crypts/
│   └── sewers/
├── taverns/
│   ├── riverside_inn.png
│   └── dwarven_brewery.png
├── wilderness/
│   ├── forests/
│   ├── mountains/
│   └── deserts/
└── urban/
    ├── streets/
    └── buildings/
```

### Best Practices
- **Categorize by theme** - dungeons, taverns, wilderness, urban
- **Descriptive naming** - `tavern_riverside_40x30.png`
- **Keep DD2VTT files** with PNG images for Foundry
- **Tag by size** - note grid dimensions in filename
- **Back up regularly** - map libraries grow fast!


## DM Tips

### Building Your Map Library
1. **Start with variety** - Get dungeons, taverns, wilderness, and urban maps
2. **Download in batches** - Clone entire repos for large collections
3. **Organize immediately** - Sort by theme as you download
4. **Keep favorites list** - Bookmark best sources for quick access
5. **Check licenses** - Know what you can use for streams/published content

### For Virtual Play
1. Test maps in your VTT before sessions
2. Import DD2VTT files for instant wall setup in Foundry
3. Keep backup generic maps for improvisation
4. Build encounter-specific folders for campaigns

### Finding Maps for Specific Needs
- **Quick Browse**: /r/battlemaps daily posts
- **Themed Collections**: GitHub repos (mbround18/vtt-maps)
- **High Quality**: Dice Grimorium, 2-Minute Tabletop
- **Community Requests**: Post in /r/battlemaps with `[Request]` tag

## DD2VTT Format

Many professional maps include `.dd2vtt` files - JSON metadata compatible with Foundry VTT:
```json
{
  "format": 0.2,
  "resolution": {
    "map_size": {"x": 40, "y": 30},
    "pixels_per_grid": 70
  },
  "line_of_sight": [...],  // Wall data
  "environment": {...}
}
```

This format provides automatic wall placement and grid alignment in Foundry VTT.

## Project Structure

```
DnDMaps/
├── map_downloader_script.py  # Interactive map downloader
├── requirements.txt           # Python dependencies (requests)
├── README.md                  # This file
├── FREE_MAP_SOURCES.md        # Complete source list
├── DOWNLOADER_GUIDE.md        # Detailed downloader instructions
├── SUMMARY.md                 # Project overview
└── maps/                      # Your downloaded maps
    ├── beach/
    ├── dungeons/
    ├── taverns/
    └── ... (organized by category)
```


## Contributing

Contributions welcome! Help us expand the resource:
- **Add map sources** - Know a great free map site? Add it to FREE_MAP_SOURCES.md
- **Improve downloader** - Better automation for bulk downloads
- **Organization tools** - Scripts for categorizing and tagging maps
- **VTT guides** - Platform-specific import tutorials
- **Licensing info** - Help track usage rights for sources

### How to Contribute
1. Fork the repository
2. Add new sources or tools
3. Test thoroughly
4. Submit a pull request

## License

This repository is open source. **Individual map licenses vary** - always check the license of downloaded maps before commercial use or streaming.

## Credits

- **Map Artists** - All the talented creators sharing their work for free
- **mbround18/vtt-maps** - Excellent DD2VTT format repository
- **Dice Grimorium** - Beautiful hand-drawn maps
- **Community** - /r/battlemaps, /r/dndmaps, and all contributors

## Links

- **Repository**: https://github.com/SnikSec/DnDMaps
- **FREE_MAP_SOURCES.md**: Complete list of free professional map sources
- **Foundry VTT DD Import**: https://foundryvtt.com/packages/dd-import
- **Issues/Suggestions**: https://github.com/SnikSec/DnDMaps/issues

---

**Happy adventuring, Dungeon Masters!** 🎲🗺️
