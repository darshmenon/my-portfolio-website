#!/usr/bin/env python3
"""
Script to create ultra-minimal footer with no boxes
"""

import re
import os

# Update CSS for no boxes - clean minimal style
def update_css(content):
    """Update CSS to remove boxes and make it ultra minimal"""
    
    # Update social-link styling to have no boxes
    content = re.sub(
        r'\.social-link \{[^}]*\}',
        '''.social-link {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.4rem 0;
            background: transparent;
            border: none;
            color: rgba(255, 255, 255, 0.7);
            text-decoration: none;
            transition: all 0.2s ease;
            font-size: 0.9rem;
            font-family: 'JetBrains Mono', monospace;
        }''',
        content
    )
    
    # Update hover state
    content = re.sub(
        r'\.social-link:hover \{[^}]*\}',
        '''.social-link:hover {
            color: #da70d6;
            transform: translateX(5px);
        }''',
        content
    )
    
    # Update grid to be more compact
    content = re.sub(
        r'\.social-links-grid \{[^}]*\}',
        '''.social-links-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 0.5rem 2rem;
            margin-bottom: 2rem;
        }''',
        content
    )
    
    return content

def update_page(filepath):
    """Update a single page with the new footer"""
    print(f"Updating {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update CSS
    content = update_css(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {filepath}")

def main():
    base_dir = "/Users/csureshkumar/my-portfolio-website"
    pages = [
        "index.html",
        "about/index.html",
        "blog/index.html",
        "contact/index.html",
        "projects/index.html",
        "robocloud-hub/index.html"
    ]
    
    for page in pages:
        filepath = os.path.join(base_dir, page)
        if os.path.exists(filepath):
            update_page(filepath)
        else:
            print(f"⚠ File not found: {filepath}")
    
    print("\n✓ All pages updated - boxes removed, ultra minimal style!")

if __name__ == "__main__":
    main()
