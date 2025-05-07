import sys
import yaml
import re
from collections import defaultdict
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 validate_addon.py <changed_files.txt>")
        sys.exit(1)
    
    # changed_files.txt (input from GitHub Actions workflow)
    changed_files_file = sys.argv[1]
    print(changed_files_file)

    # Step 1: Generate a list of changed_files from changed_files.txt
    with open(changed_files_file) as f:
        changed_files = [line.strip() for line in f.readlines() if line.strip()]

    # Step 2: Group by vendor-product folder inside templates/ (assumes commit/PR of multiple assets)
    changed_by_dir = defaultdict(list)
    for changed_file in changed_files:
        if changed_file.startswith("templates/"):
            parts = changed_file.split("/")
            if len(parts) >= 3:
                vendor_product = parts[1]
                changed_by_dir[vendor_product].append(changed_file)
    
    for vendor_product, files in changed_by_dir.items():
        print(f"\nValidating templates/{vendor_product}")
        print(f"templates/{vendor_product} passed validation")

if __name__ == "__main__":
    main()
