#!/usr/bin/env python3
"""
Clean up code: Remove pink particles, remove old footer scripts
"""

import re
import os
import glob

def main():
    base_dir = "/Users/csureshkumar/my-portfolio-website"
    
    # 1. Remove old footer update scripts
    print("Cleaning up old footer scripts...")
    old_scripts = glob.glob(os.path.join(base_dir, "update_footer*.py"))
    for script in old_scripts:
        try:
            os.remove(script)
            print(f"✓ Removed {os.path.basename(script)}")
        except Exception as e:
            print(f"⚠ Could not remove {script}: {e}")
    
    # 2. Fix pink particles in all HTML files
    print("\nFixing pink particles in HTML files...")
    html_files = [
        "index.html",
        "about/index.html",
        "blog/index.html",
        "contact/index.html",
        "projects/index.html",
        "robocloud-hub/index.html"
    ]
    
    for html_file in html_files:
        filepath = os.path.join(base_dir, html_file)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Change particle background from pink to white in CSS
        content = re.sub(
            r'(\.particle \{[^}]*?background:\s*)[^;]+',
            r'\1#ffffff',
            content,
            flags=re.DOTALL
        )
        
        # Also reduce opacity for white particles
        content = re.sub(
            r'(\.particle \{[^}]*?opacity:\s*)\d+\.?\d*',
            r'\g<1>0.3',
            content,
            flags=re.DOTALL
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Fixed {html_file}")
    
    print("\n✓ Cleanup complete!")
    print("\nSummary:")
    print("- Removed old footer update scripts")
    print("- Changed particle colors from pink (#da70d6) to white (#ffffff)")
    print("- Adjusted particle opacity for better visibility")

if __name__ == "__main__":
    main()
