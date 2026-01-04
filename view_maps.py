"""
DD2VTT Map Viewer (Free - No VTT Required)
Extracts and displays maps from DD2VTT files
"""

import json
import base64
from pathlib import Path
from PIL import Image
from io import BytesIO
import os


def extract_image_from_dd2vtt(dd2vtt_path: Path) -> Image.Image:
    """Extract PNG image from DD2VTT file"""
    with open(dd2vtt_path, 'r') as f:
        data = json.load(f)
    
    # DD2VTT files have base64-encoded image in 'image' field
    image_data = base64.b64decode(data['image'])
    return Image.open(BytesIO(image_data))


def get_map_info(dd2vtt_path: Path) -> dict:
    """Get map metadata from DD2VTT file"""
    with open(dd2vtt_path, 'r') as f:
        data = json.load(f)
    
    resolution = data.get('resolution', {})
    map_size = resolution.get('map_size', {})
    
    return {
        'name': dd2vtt_path.stem,
        'grid_width': map_size.get('x', 'unknown'),
        'grid_height': map_size.get('y', 'unknown'),
        'pixels_per_grid': resolution.get('pixels_per_grid', 'unknown')
    }


def export_map_to_png(dd2vtt_path: Path, output_dir: Path = None):
    """Export DD2VTT map to PNG file"""
    if output_dir is None:
        output_dir = dd2vtt_path.parent / "exported_pngs"
    
    output_dir.mkdir(exist_ok=True)
    
    image = extract_image_from_dd2vtt(dd2vtt_path)
    output_path = output_dir / f"{dd2vtt_path.stem}.png"
    image.save(output_path)
    
    return output_path


def export_all_maps(maps_dir: Path = Path("maps")):
    """Export all DD2VTT files to PNG"""
    exported = []
    
    print("=" * 70)
    print("Exporting DD2VTT maps to PNG files...")
    print("=" * 70)
    
    for dd2vtt_file in maps_dir.rglob("*.dd2vtt"):
        try:
            print(f"\n📄 Processing: {dd2vtt_file.relative_to(maps_dir)}")
            
            # Get map info
            info = get_map_info(dd2vtt_file)
            print(f"   Grid: {info['grid_width']}x{info['grid_height']} @ {info['pixels_per_grid']}px per square")
            
            # Export to PNG
            output_path = export_map_to_png(dd2vtt_file)
            print(f"   ✓ Exported: {output_path}")
            
            exported.append({
                'name': info['name'],
                'category': dd2vtt_file.parent.name,
                'png_path': str(output_path),
                'info': info
            })
            
        except Exception as e:
            print(f"   ✗ Failed: {e}")
    
    return exported


def view_map(dd2vtt_path: Path):
    """Open and display a single map"""
    print(f"\nOpening: {dd2vtt_path.name}")
    
    # Get info
    info = get_map_info(dd2vtt_path)
    print(f"Grid: {info['grid_width']}x{info['grid_height']}")
    print(f"Pixels per square: {info['pixels_per_grid']}")
    
    # Extract and show image
    image = extract_image_from_dd2vtt(dd2vtt_path)
    image.show()


def list_all_maps(maps_dir: Path = Path("maps")):
    """List all available maps"""
    maps_by_category = {}
    
    for dd2vtt_file in maps_dir.rglob("*.dd2vtt"):
        category = dd2vtt_file.parent.name
        if category not in maps_by_category:
            maps_by_category[category] = []
        
        info = get_map_info(dd2vtt_file)
        maps_by_category[category].append({
            'name': info['name'],
            'path': dd2vtt_file,
            'grid': f"{info['grid_width']}x{info['grid_height']}"
        })
    
    return maps_by_category


def main():
    """Interactive map viewer"""
    print("=" * 70)
    print(" DD2VTT Map Viewer - View maps without VTT software!")
    print("=" * 70)
    
    maps_dir = Path("maps")
    
    if not maps_dir.exists():
        print("\n❌ No maps folder found. Run map_downloader_script.py first!")
        return
    
    print("\nSelect viewing mode:")
    print("  1. Export all maps to PNG files")
    print("  2. View single map")
    print("  3. List all available maps")
    
    try:
        choice = input("\nEnter choice (1-3): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\nExiting...")
        return
    
    if choice == "1":
        exported = export_all_maps(maps_dir)
        
        print("\n" + "=" * 70)
        print(f"✓ Exported {len(exported)} maps")
        print("=" * 70)
        print("\nPNG files saved in each category's 'exported_pngs' folder")
        print("You can now open them with any image viewer!")
        
        # Show where files are
        categories = set(m['category'] for m in exported)
        print("\nExported to:")
        for cat in sorted(categories):
            print(f"  maps/{cat}/exported_pngs/")
    
    elif choice == "2":
        # List maps
        maps = list_all_maps(maps_dir)
        
        print("\nAvailable maps:")
        all_maps = []
        idx = 1
        for category in sorted(maps.keys()):
            print(f"\n  {category}:")
            for map_info in maps[category]:
                print(f"    {idx}. {map_info['name']} ({map_info['grid']})")
                all_maps.append(map_info)
                idx += 1
        
        try:
            map_num = int(input("\nEnter map number to view: ").strip())
            if 1 <= map_num <= len(all_maps):
                view_map(all_maps[map_num - 1]['path'])
            else:
                print("Invalid map number")
        except (ValueError, EOFError, KeyboardInterrupt):
            print("\nCancelled")
    
    elif choice == "3":
        maps = list_all_maps(maps_dir)
        
        print("\n" + "=" * 70)
        print("Available Maps:")
        print("=" * 70)
        
        total = 0
        for category in sorted(maps.keys()):
            print(f"\n📁 {category} ({len(maps[category])} maps)")
            for map_info in maps[category]:
                print(f"   • {map_info['name']:30} {map_info['grid']}")
                total += 1
        
        print("\n" + "=" * 70)
        print(f"Total: {total} maps")
        print("=" * 70)
    
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
