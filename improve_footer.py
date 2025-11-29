#!/usr/bin/env python3
"""
Improve footer: more spacing and consistent colors
"""

import re
import os

def update_footer_css(content):
    """Update footer CSS for better spacing and consistent colors"""
    
    # Update social-links-grid for more spacing
    content = re.sub(
        r'\.social-links-grid \{[^}]*\}',
        '''.social-links-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 1.2rem 2rem;
            margin-bottom: 0;
        }''',
        content
    )
    
    # Update social-link for consistent colors
    content = re.sub(
        r'\.social-link \{[^}]*\}',
        '''.social-link {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.7rem 0;
            background: transparent;
            border: none;
            color: #9370db;
            text-decoration: none;
            transition: all 0.2s ease;
            font-size: 0.85rem;
            font-family: 'JetBrains Mono', monospace;
        }''',
        content
    )
    
    # Update hover state for consistent color
    content = re.sub(
        r'\.social-link:hover \{[^}]*\}',
        '''.social-link:hover {
            color: #da70d6;
            transform: translateX(6px);
        }''',
        content
    )
    
    # Update cmd-symbol for consistent color
    content = re.sub(
        r'\.cmd-symbol \{[^}]*\}',
        '''.cmd-symbol {
            color: #9370db;
            font-weight: 700;
        }''',
        content
    )
    
    # Update cmd-symbol hover for consistent color
    content = re.sub(
        r'\.social-link:hover \.cmd-symbol \{[^}]*\}',
        '''.social-link:hover .cmd-symbol {
            color: #da70d6;
        }''',
        content
    )
    
    # Update terminal-body padding for more space
    content = re.sub(
        r'\.terminal-body \{[^}]*\}',
        '''.terminal-body {
            padding: 2.5rem 2rem;
        }''',
        content
    )
    
    # Update mobile spacing
    pattern = r'@media \(max-width: 768px\) \{[^}]*\.social-links-grid \{[^}]*\}[^}]*\}'
    mobile_css = '''@media (max-width: 768px) {
            .terminal-body {
                padding: 2rem 1.5rem;
            }

            .social-links-grid {
                grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
                gap: 1rem 1.5rem;
            }

            .social-link {
                font-size: 0.8rem;
                padding: 0.6rem 0;
            }
        }'''
    
    # Find and replace mobile media query section
    if '@media (max-width: 768px)' in content:
        # Find the terminal styles media query and replace it
        content = re.sub(
            r'@media \(max-width: 768px\) \{[^}]*?\.terminal-body[^}]*?\}[^}]*?\.social-links-grid[^}]*?\}[^}]*?\.social-link[^}]*?\}[^}]*?\}',
            mobile_css,
            content,
            flags=re.DOTALL
        )
    
    return content

def update_page(filepath):
    """Update a single page"""
    print(f"Updating {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update CSS
    content = update_footer_css(content)
    
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
    
    print("\n✓ All pages updated with better spacing and consistent colors!")

if __name__ == "__main__":
    main()
