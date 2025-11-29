#!/usr/bin/env python3
"""
Script to use emojis instead of Font Awesome icons and add Chess.com
"""

import re
import os

# New footer HTML with emojis and Chess.com
NEW_FOOTER_HTML = """    <footer class="footer">
        <div class="footer-content">
            <div class="social-links-section">
                <h3>CONNECT WITH ME</h3>
                <div class="social-links-grid">
                    <a href="https://robocloud-dashboard.vercel.app" target="_blank" class="social-link">
                        <span class="emoji-icon">🤖</span>
                        <span>RoboCloud App</span>
                    </a>
                    <a href="https://github.com/darshmenon" target="_blank" class="social-link">
                        <span class="emoji-icon">💻</span>
                        <span>GitHub</span>
                    </a>
                    <a href="https://linkedin.com/in/darsh-menon" target="_blank" class="social-link">
                        <span class="emoji-icon">💼</span>
                        <span>LinkedIn</span>
                    </a>
                    <a href="https://x.com/darsh_menon" target="_blank" class="social-link">
                        <span class="emoji-icon">🐦</span>
                        <span>X - @darsh_menon</span>
                    </a>
                    <a href="https://x.com/Darsh_Menon_08" target="_blank" class="social-link">
                        <span class="emoji-icon">🐦</span>
                        <span>X - @Darsh_Menon_08</span>
                    </a>
                    <a href="https://medium.com/@darshmenon02" target="_blank" class="social-link">
                        <span class="emoji-icon">📝</span>
                        <span>Medium</span>
                    </a>
                    <a href="https://www.youtube.com/@darshmenon0008" target="_blank" class="social-link">
                        <span class="emoji-icon">📺</span>
                        <span>YouTube</span>
                    </a>
                    <a href="https://instagram.com/_.darshmenon._" target="_blank" class="social-link">
                        <span class="emoji-icon">📷</span>
                        <span>Instagram</span>
                    </a>
                    <a href="https://open.spotify.com/user/31qiavd6dklz2jp5zvhmbl63eu74" target="_blank" class="social-link">
                        <span class="emoji-icon">🎵</span>
                        <span>Spotify</span>
                    </a>
                    <a href="https://facebook.com/darsh.menon.9" target="_blank" class="social-link">
                        <span class="emoji-icon">👥</span>
                        <span>Facebook</span>
                    </a>
                    <a href="https://in.pinterest.com/darshmenon/" target="_blank" class="social-link">
                        <span class="emoji-icon">📌</span>
                        <span>Pinterest</span>
                    </a>
                    <a href="https://www.chess.com/member/darshthegreat" target="_blank" class="social-link">
                        <span class="emoji-icon">♟️</span>
                        <span>Chess.com</span>
                    </a>
                </div>
            </div>
            
            <div class="footer-info">
                <p>© 2025 Darsh Menon - Robotics Software Engineer | BITS Pilani Graduate | Asimov Robotics</p>
                <p>"The only way to do great work is to love what you do." – Steve Jobs</p>
                <p>Specializing in ROS2, Autonomous Systems, Computer Vision & AI-driven Robotics</p>
            </div>
        </div>
    </footer>"""

def update_page(filepath):
    """Update a single page with the new footer"""
    print(f"Updating {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update HTML footer content
    old_footer_pattern = r'<footer class="footer">.*?</footer>'
    content = re.sub(old_footer_pattern, NEW_FOOTER_HTML, content, flags=re.DOTALL)
    
    # Update CSS to style emoji icons
    emoji_icon_css = """
        .emoji-icon {
            font-size: 1.3rem;
            min-width: 24px;
            text-align: center;
        }
"""
    
    # Add emoji-icon CSS if not already present
    if '.emoji-icon' not in content:
        # Insert after .social-link i styles
        content = re.sub(
            r'(\.social-link:hover i \{[^}]*\})',
            r'\1\n' + emoji_icon_css,
            content
        )
    
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
    
    print("\n✓ All pages updated with emoji icons and Chess.com added!")

if __name__ == "__main__":
    main()
