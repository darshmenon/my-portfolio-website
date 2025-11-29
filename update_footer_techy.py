#!/usr/bin/env python3
"""
Script to create minimalistic techy/coding style footer
"""

import re
import os

# New footer HTML with minimalistic coding aesthetic
NEW_FOOTER_HTML = """    <footer class="footer">
        <div class="footer-content">
            <div class="social-links-section">
                <h3>// CONNECT</h3>
                <div class="social-links-grid">
                    <a href="https://robocloud-dashboard.vercel.app" target="_blank" class="social-link">
                        <span class="link-prefix">></span> RoboCloud
                    </a>
                    <a href="https://github.com/darshmenon" target="_blank" class="social-link">
                        <span class="link-prefix">></span> GitHub
                    </a>
                    <a href="https://linkedin.com/in/darsh-menon" target="_blank" class="social-link">
                        <span class="link-prefix">></span> LinkedIn
                    </a>
                    <a href="https://x.com/darsh_menon" target="_blank" class="social-link">
                        <span class="link-prefix">></span> X @darsh_menon
                    </a>
                    <a href="https://x.com/Darsh_Menon_08" target="_blank" class="social-link">
                        <span class="link-prefix">></span> X @Darsh_Menon_08
                    </a>
                    <a href="https://medium.com/@darshmenon02" target="_blank" class="social-link">
                        <span class="link-prefix">></span> Medium
                    </a>
                    <a href="https://www.youtube.com/@darshmenon0008" target="_blank" class="social-link">
                        <span class="link-prefix">></span> YouTube
                    </a>
                    <a href="https://instagram.com/_.darshmenon._" target="_blank" class="social-link">
                        <span class="link-prefix">></span> Instagram
                    </a>
                    <a href="https://open.spotify.com/user/31qiavd6dklz2jp5zvhmbl63eu74" target="_blank" class="social-link">
                        <span class="link-prefix">></span> Spotify
                    </a>
                    <a href="https://facebook.com/darsh.menon.9" target="_blank" class="social-link">
                        <span class="link-prefix">></span> Facebook
                    </a>
                    <a href="https://in.pinterest.com/darshmenon/" target="_blank" class="social-link">
                        <span class="link-prefix">></span> Pinterest
                    </a>
                    <a href="https://www.chess.com/member/darshthegreat" target="_blank" class="social-link">
                        <span class="link-prefix">></span> Chess.com
                    </a>
                </div>
            </div>
            
            <div class="footer-info">
                <p>© 2025 Darsh Menon // Robotics Software Engineer</p>
                <p>BITS Pilani Graduate | Asimov Robotics</p>
            </div>
        </div>
    </footer>"""

# Update CSS for minimalistic techy style
def update_css(content):
    """Update CSS to be more minimalistic and techy"""
    
    # Update social-links-section h3 styling to be more minimal
    content = re.sub(
        r'\.social-links-section h3 \{[^}]*\}',
        '''.social-links-section h3 {
            color: #da70d6;
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
            font-weight: 600;
            letter-spacing: 3px;
            font-family: 'JetBrains Mono', monospace;
        }''',
        content
    )
    
    # Update social-link styling to be minimal
    content = re.sub(
        r'\.social-link \{[^}]*\}',
        '''.social-link {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.6rem 1rem;
            background: transparent;
            border: 1px solid rgba(147, 112, 219, 0.2);
            border-radius: 4px;
            color: rgba(255, 255, 255, 0.8);
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
            background: rgba(147, 112, 219, 0.05);
            border-color: #da70d6;
            color: #ffffff;
            transform: translateX(4px);
        }''',
        content
    )
    
    # Add link-prefix styling if not present
    if '.link-prefix' not in content:
        link_prefix_css = '''
        .link-prefix {
            color: #da70d6;
            font-weight: 700;
            opacity: 0.6;
        }
        
        .social-link:hover .link-prefix {
            opacity: 1;
        }
'''
        # Insert after social-link:hover
        content = re.sub(
            r'(\.social-link:hover \{[^}]*\})',
            r'\1' + link_prefix_css,
            content
        )
    
    return content

def update_page(filepath):
    """Update a single page with the new footer"""
    print(f"Updating {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update HTML footer content
    old_footer_pattern = r'<footer class="footer">.*?</footer>'
    content = re.sub(old_footer_pattern, NEW_FOOTER_HTML, content, flags=re.DOTALL)
    
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
    
    print("\n✓ All pages updated with minimalistic techy footer!")

if __name__ == "__main__":
    main()
