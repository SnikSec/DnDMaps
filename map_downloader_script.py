"""
Map Downloader Script
Downloads professional D&D maps from free sources (mbround18/vtt-maps GitHub repo)
"""

import os
import requests
from pathlib import Path
from typing import List, Dict
import json
import time


class MapDownloader:
    """Download maps from mbround18/vtt-maps GitHub repository"""
    
    def __init__(self, output_dir: str = "maps"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.github_api_base = "https://api.github.com/repos/mbround18/vtt-maps/contents/maps"
        self.github_raw_base = "https://raw.githubusercontent.com/mbround18/vtt-maps/main/maps"
        
        # Available categories in the mbround18 repo
        self.categories = [
            'beach', 'dungeons', 'forest', 'taverns', 'locations',
            'encounters', 'travel', 'desert', 'tundra', 'cyberpunk',
            'base_building', 'spires', 'other'
        ]
    
    def get_category_contents(self, category: str) -> List[Dict]:
        """Get list of all items in a category folder"""
        url = f"{self.github_api_base}/{category}"
        print(f"📂 Scanning {category} folder...")
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"  ✗ Failed to access {category}: {e}")
            return []
    
    def download_file(self, file_url: str, save_path: Path) -> bool:
        """Download a single file from URL"""
        try:
            response = requests.get(file_url, timeout=60)
            response.raise_for_status()
            
            save_path.parent.mkdir(parents=True, exist_ok=True)
            save_path.write_bytes(response.content)
            return True
        except Exception as e:
            print(f"    ✗ Failed: {e}")
            return False
    
    def download_map_from_category(self, category: str, map_name: str) -> bool:
        """
        Download a specific map (DD2VTT file) from a category
        
        Args:
            category: Category folder name (e.g., 'beach', 'dungeons')
            map_name: Map filename without extension (e.g., 'simple-beach')
        
        Returns:
            True if successful, False otherwise
        """
        dd2vtt_filename = f"{map_name}.dd2vtt"
        dd2vtt_url = f"{self.github_raw_base}/{category}/{dd2vtt_filename}"
        
        # Create category subfolder
        category_dir = self.output_dir / category
        category_dir.mkdir(exist_ok=True)
        
        save_path = category_dir / dd2vtt_filename
        
        print(f"  📥 Downloading {map_name}...")
        
        if self.download_file(dd2vtt_url, save_path):
            print(f"    ✓ Saved DD2VTT: {save_path}")
            
            # Also try to download the .md description file
            md_filename = f"{map_name}.md"
            md_url = f"{self.github_raw_base}/{category}/{md_filename}"
            md_path = category_dir / md_filename
            
            if self.download_file(md_url, md_path):
                print(f"    ✓ Saved description: {md_filename}")
            
            return True
        return False
    
    def discover_and_download_category(self, category: str, limit: int = None) -> int:
        """
        Discover all maps in a category and download them
        
        Args:
            category: Category name (e.g., 'beach', 'dungeons')
            limit: Maximum number of maps to download (None for all)
        
        Returns:
            Number of maps successfully downloaded
        """
        contents = self.get_category_contents(category)
        if not contents:
            return 0
        
        # Filter for .dd2vtt files
        dd2vtt_files = [
            item for item in contents 
            if item['type'] == 'file' and item['name'].endswith('.dd2vtt')
        ]
        
        print(f"  Found {len(dd2vtt_files)} maps in {category}")
        
        if limit:
            dd2vtt_files = dd2vtt_files[:limit]
            print(f"  Limiting to {limit} maps")
        
        downloaded = 0
        for item in dd2vtt_files:
            map_name = item['name'].replace('.dd2vtt', '')
            if self.download_map_from_category(category, map_name):
                downloaded += 1
                time.sleep(0.5)  # Be nice to GitHub
        
        return downloaded
    
    def download_all_categories(self, limit_per_category: int = None) -> Dict[str, int]:
        """
        Download maps from all available categories
        
        Args:
            limit_per_category: Max maps per category (None for all)
        
        Returns:
            Dictionary with category names and download counts
        """
        results = {}
        
        for category in self.categories:
            print(f"\n{'='*60}")
            print(f"Category: {category}")
            print(f"{'='*60}")
            
            downloaded = self.discover_and_download_category(category, limit_per_category)
            results[category] = downloaded
            
            print(f"✓ Downloaded {downloaded} maps from {category}\n")
        
        return results
    
    def create_index(self):
        """Create an index of all downloaded maps"""
        index = {}
        total_maps = 0
        
        for category_dir in self.output_dir.iterdir():
            if category_dir.is_dir():
                category = category_dir.name
                maps_list = []
                
                for dd2vtt_file in category_dir.glob('*.dd2vtt'):
                    map_info = {
                        'name': dd2vtt_file.stem,
                        'dd2vtt_file': str(dd2vtt_file),
                        'has_description': (dd2vtt_file.with_suffix('.md')).exists()
                    }
                    maps_list.append(map_info)
                    total_maps += 1
                
                if maps_list:
                    index[category] = maps_list
        
        # Save index
        index_file = self.output_dir / 'index.json'
        with open(index_file, 'w') as f:
            json.dump(index, f, indent=2)
        
        print(f"\n✓ Index created: {index_file}")
        print(f"✓ Total maps catalogued: {total_maps}")
        return index


def main():
    """Download maps from mbround18/vtt-maps repository"""
    
    print("=" * 70)
    print(" D&D Map Downloader - mbround18/vtt-maps")
    print(" Professional DungeonDraft Maps with DD2VTT Format")
    print("=" * 70)
    
    downloader = MapDownloader()
    
    print("\nSelect download mode:")
    print("  1. Download sample maps (2 per category)")
    print("  2. Download all maps from specific categories")
    print("  3. Download ALL maps (may take a while!)")
    print("  4. Download specific map")
    
    try:
        choice = input("\nEnter choice (1-4): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\nDefaulting to option 1 (sample maps)")
        choice = "1"
    
    print()
    
    if choice == "1":
        print("📦 Downloading sample maps (2 from each category)...\n")
        results = downloader.download_all_categories(limit_per_category=2)
    
    elif choice == "2":
        print("Available categories:")
        for i, cat in enumerate(downloader.categories, 1):
            print(f"  {i}. {cat}")
        
        try:
            cat_nums = input("\nEnter category numbers (comma-separated, e.g., 1,3,5): ").strip()
            selected_indices = [int(n.strip()) - 1 for n in cat_nums.split(',')]
            selected_categories = [downloader.categories[i] for i in selected_indices if 0 <= i < len(downloader.categories)]
        except:
            print("Invalid input, downloading from 'dungeons' and 'taverns'")
            selected_categories = ['dungeons', 'taverns']
        
        results = {}
        for category in selected_categories:
            print(f"\n{'='*60}")
            print(f"Category: {category}")
            print(f"{'='*60}")
            downloaded = downloader.discover_and_download_category(category)
            results[category] = downloaded
    
    elif choice == "3":
        print("⚠️  This will download ALL maps from the repository!")
        try:
            confirm = input("Continue? (yes/no): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            confirm = "no"
        
        if confirm == 'yes':
            print("\n📦 Downloading all maps...\n")
            results = downloader.download_all_categories()
        else:
            print("Cancelled.")
            return
    
    elif choice == "4":
        print("\nExample: To download 'simple-beach' from 'beach' category")
        try:
            category = input("Category name: ").strip()
            map_name = input("Map name (without extension): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")
            return
        
        if category in downloader.categories:
            success = downloader.download_map_from_category(category, map_name)
            results = {category: 1 if success else 0}
        else:
            print(f"Invalid category. Available: {', '.join(downloader.categories)}")
            return
    
    else:
        print("Invalid choice. Run the script again.")
        return
    
    # Create index
    print("\n" + "=" * 70)
    print("Creating map index...")
    print("=" * 70)
    index = downloader.create_index()
    
    # Summary
    print("\n" + "=" * 70)
    print("Download Summary:")
    print("=" * 70)
    
    total_downloaded = sum(results.values())
    for category, count in results.items():
        print(f"  {category}: {count} maps")
    
    print(f"\n✓ Total maps downloaded: {total_downloaded}")
    print(f"✓ Maps saved to: {downloader.output_dir}/")
    print(f"✓ Index saved to: {downloader.output_dir}/index.json")
    
    print("\n" + "=" * 70)
    print("Next Steps:")
    print("=" * 70)
    print("• Maps are ready to use in your VTT!")
    print("• DD2VTT files can be imported directly into Foundry VTT")
    print("• Use the DD Import module: https://foundryvtt.com/packages/dd-import/")
    print("• .md files contain map descriptions and details")
    print("=" * 70)


if __name__ == "__main__":
    main()
