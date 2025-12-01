"""
Make ALL fonts JetBrains Mono for MAXIMUM tech-geek aesthetic
"""

import os
import re

def make_fonts_techy(filepath):
    """Replace font family with JetBrains Mono everywhere"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        original_content = content
        
        # Replace Plus Jakarta Sans with JetBrains Mono
        content = content.replace(
            "font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;",
            "font-family: 'JetBrains Mono', monospace !important;"
        )
        
        # Replace Space Grotesk with JetBrains Mono
        content = content.replace(
            "font-family: 'Space Grotesk', 'Inter', sans-serif !important;",
            "font-family: 'JetBrains Mono', monospace !important;"
        )
        
        if content != original_content:
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"✅ Made fonts techy in {filepath}")
        else:
            print(f"⏭️  No font changes needed in {filepath}")
            
    except Exception as e:
        print(f"❌ Error with {filepath}: {e}")

# Apply to all HTML pages
pages = [
    '/Users/csureshkumar/my-portfolio-website/index.html',
    '/Users/csureshkumar/my-portfolio-website/about/index.html',
    '/Users/csureshkumar/my-portfolio-website/projects/index.html',
    '/Users/csureshkumar/my-portfolio-website/blog/index.html',
    '/Users/csureshkumar/my-portfolio-website/contact/index.html',
    '/Users/csureshkumar/my-portfolio-website/robocloud-hub/index.html',
]

for page in pages:
    if os.path.exists(page):
        make_fonts_techy(page)

print("\n🤓 ALL pages now use JetBrains Mono for MAXIMUM TECH-GEEK aesthetic!")
