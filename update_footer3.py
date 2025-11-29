#!/usr/bin/env python3
"""
Script to restore icons and add second X account
"""

import re
import os

# New footer HTML content WITH icons and both X accounts
NEW_FOOTER_HTML = """    <footer class="footer">
        <div class="footer-content">
            <div class="social-links-section">
                <h3>CONNECT WITH ME</h3>
                <div class="social-links-grid">
                    <a href="https://robocloud-dashboard.vercel.app" target="_blank" class="social-link">
                        <i class="fas fa-robot"></i>
                        <span>RoboCloud App</span>
                    </a>
                    <a href="https://github.com/darshmenon" target="_blank" class="social-link">
                        <i class="fab fa-github"></i>
                        <span>GitHub</span>
                    </a>
                    <a href="https://linkedin.com/in/darsh-menon" target="_blank" class="social-link">
                        <i class="fab fa-linkedin"></i>
                        <span>LinkedIn</span>
                    </a>
                    <a href="https://x.com/darsh_menon" target="_blank" class="social-link">
                        <i class="fab fa-x-twitter"></i>
                        <span>X - @darsh_menon</span>
                    </a>
                    <a href="https://x.com/Darsh_Menon_08" target="_blank" class="social-link">
                        <i class="fab fa-x-twitter"></i>
                        <span>X - @Darsh_Menon_08</span>
                    </a>
                    <a href="https://medium.com/@darshmenon02" target="_blank" class="social-link">
                        <i class="fab fa-medium"></i>
                        <span>Medium</span>
                    </a>
                    <a href="https://www.youtube.com/@darshmenon0008" target="_blank" class="social-link">
                        <i class="fab fa-youtube"></i>
                        <span>YouTube</span>
                    </a>
                    <a href="https://instagram.com/_.darshmenon._" target="_blank" class="social-link">
                        <i class="fab fa-instagram"></i>
                        <span>Instagram</span>
                    </a>
                    <a href="https://open.spotify.com/user/31qiavd6dklz2jp5zvhmbl63eu74" target="_blank" class="social-link">
                        <i class="fab fa-spotify"></i>
                        <span>Spotify</span>
                    </a>
                    <a href="https://facebook.com/darsh.menon.9" target="_blank" class="social-link">
                        <i class="fab fa-facebook"></i>
                        <span>Facebook</span>
                    </a>
                    <a href="https://in.pinterest.com/darshmenon/" target="_blank" class="social-link">
                        <i class="fab fa-pinterest"></i>
                        <span>Pinterest</span>
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
    
    print("\n✓ All pages updated with icons restored and second X account added!")

if __name__ == "__main__":
    main()
