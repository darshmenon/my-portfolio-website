#!/usr/bin/env python3
"""
Script to update footer on all pages with social media links
"""

import re
import os

# The CSS to add after the main .footer block
FOOTER_ADDITIONAL_CSS = """
        .footer p {
            margin: 0.5rem 0;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
        }

        .social-links-section {
            margin: 2rem 0;
        }

        .social-links-section h3 {
            color: #da70d6;
            font-size: 1.3rem;
            margin-bottom: 1.5rem;
            text-shadow: 0 0 20px rgba(147, 112, 219, 0.6);
            font-weight: 700;
            letter-spacing: 2px;
        }

        .social-links-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .social-link {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            padding: 1rem 1.5rem;
            background: rgba(147, 112, 219, 0.1);
            border: 1px solid rgba(147, 112, 219, 0.3);
            border-radius: 12px;
            color: #ffffff;
            text-decoration: none;
            transition: all 0.3s ease;
            font-size: 0.95rem;
            backdrop-filter: blur(10px);
        }

        .social-link:hover {
            background: rgba(147, 112, 219, 0.2);
            border-color: #da70d6;
            transform: translateY(-3px);
            box-shadow: 0 5px 20px rgba(147, 112, 219, 0.4);
        }

        .social-link i {
            font-size: 1.3rem;
            color: #da70d6;
            min-width: 24px;
            text-align: center;
        }

        .social-link:hover i {
            color: #ba55d3;
            text-shadow: 0 0 10px rgba(186, 85, 211, 0.8);
        }

        .footer-info {
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(147, 112, 219, 0.2);
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.7);
        }

        @media (max-width: 768px) {
            .social-links-grid {
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 1rem;
            }

            .social-link {
                padding: 0.8rem 1rem;
                font-size: 0.85rem;
            }

            .social-link i {
                font-size: 1.1rem;
            }
        }
"""

# New footer HTML content
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
                        <span>X (Twitter)</span>
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
    
    # Update CSS - make footer text-align: center and add new styles
    # First, update the main .footer block
    content = re.sub(
        r'(\.footer\s*\{[^}]*?)text-align:\s*left;',
        r'\1text-align: center;',
        content
    )
    content = re.sub(
        r'(\.footer\s*\{[^}]*?)font-size:\s*1\.2rem;',
        r'\1font-size: 1rem;',
        content
    )
    
    # Add new footer styles after the .footer block
    # Find where .footer block ends and insert new styles
    footer_css_pattern = r'(\.footer\s*\{[^}]*\})'
    match = re.search(footer_css_pattern, content)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + '\n' + FOOTER_ADDITIONAL_CSS + '\n' + content[insert_pos:]
    
    # Update HTML footer content
    old_footer_pattern = r'<footer class="footer">.*?</footer>'
    content = re.sub(old_footer_pattern, NEW_FOOTER_HTML, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {filepath}")

def main():
    base_dir = "/Users/csureshkumar/my-portfolio-website"
    pages = [
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
    
    print("\n✓ All pages updated successfully!")

if __name__ == "__main__":
    main()
