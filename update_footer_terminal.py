#!/usr/bin/env python3
"""
Script to create modern terminal-style footer with better UI design
"""

import re
import os

# New footer HTML with modern terminal aesthetic
NEW_FOOTER_HTML = """    <footer class="footer">
        <div class="footer-content">
            <div class="footer-terminal">
                <div class="terminal-header">
                    <span class="terminal-title">darsh@connect:~$</span>
                </div>
                <div class="terminal-body">
                    <div class="social-links-grid">
                        <a href="https://robocloud-dashboard.vercel.app" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./robocloud
                        </a>
                        <a href="https://github.com/darshmenon" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./github
                        </a>
                        <a href="https://linkedin.com/in/darsh-menon" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./linkedin
                        </a>
                        <a href="https://x.com/darsh_menon" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./x_main
                        </a>
                        <a href="https://x.com/Darsh_Menon_08" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./x_alt
                        </a>
                        <a href="https://medium.com/@darshmenon02" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./medium
                        </a>
                        <a href="https://www.youtube.com/@darshmenon0008" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./youtube
                        </a>
                        <a href="https://instagram.com/_.darshmenon._" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./instagram
                        </a>
                        <a href="https://open.spotify.com/user/31qiavd6dklz2jp5zvhmbl63eu74" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./spotify
                        </a>
                        <a href="https://facebook.com/darsh.menon.9" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./facebook
                        </a>
                        <a href="https://in.pinterest.com/darshmenon/" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./pinterest
                        </a>
                        <a href="https://www.chess.com/member/darshthegreat" target="_blank" class="social-link">
                            <span class="cmd-symbol">$</span> ./chess
                        </a>
                    </div>
                </div>
            </div>
            
            <div class="footer-info">
                <p>© 2025 Darsh Menon | Robotics Software Engineer | BITS Pilani | Asimov Robotics</p>
            </div>
        </div>
    </footer>"""

# CSS for modern terminal style
TERMINAL_CSS = """
        .footer-terminal {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(147, 112, 219, 0.3);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 2rem;
            backdrop-filter: blur(10px);
        }

        .terminal-header {
            background: rgba(147, 112, 219, 0.1);
            padding: 0.8rem 1.2rem;
            border-bottom: 1px solid rgba(147, 112, 219, 0.2);
        }

        .terminal-title {
            color: #da70d6;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            font-weight: 600;
        }

        .terminal-body {
            padding: 2rem 1.5rem;
        }

        .social-links-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 0.8rem 1.5rem;
            margin-bottom: 0;
        }

        .social-link {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 0;
            background: transparent;
            border: none;
            color: rgba(255, 255, 255, 0.75);
            text-decoration: none;
            transition: all 0.2s ease;
            font-size: 0.85rem;
            font-family: 'JetBrains Mono', monospace;
        }

        .social-link:hover {
            color: #da70d6;
            transform: translateX(6px);
        }

        .cmd-symbol {
            color: #9370db;
            font-weight: 700;
        }

        .social-link:hover .cmd-symbol {
            color: #ba55d3;
        }

        .footer-info {
            margin-top: 1.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(147, 112, 219, 0.2);
            font-size: 0.85rem;
            color: rgba(255, 255, 255, 0.6);
            text-align: center;
        }

        .footer-info p {
            margin: 0.3rem 0;
        }

        @media (max-width: 768px) {
            .terminal-body {
                padding: 1.5rem 1rem;
            }

            .social-links-grid {
                grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
                gap: 0.6rem 1rem;
            }

            .social-link {
                font-size: 0.8rem;
            }
        }
"""

def update_page(filepath):
    """Update a single page with the new footer"""
    print(f"Updating {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update HTML footer content
    old_footer_pattern = r'<footer class="footer">.*?</footer>'
    content = re.sub(old_footer_pattern, NEW_FOOTER_HTML, content, flags=re.DOTALL)
    
    # Remove old terminal-related CSS if it exists
    content = re.sub(r'\.footer-terminal \{[^}]*\}', '', content)
    content = re.sub(r'\.terminal-header \{[^}]*\}', '', content)
    content = re.sub(r'\.terminal-title \{[^}]*\}', '', content)
    content = re.sub(r'\.terminal-body \{[^}]*\}', '', content)
    content = re.sub(r'\.cmd-symbol \{[^}]*\}', '', content)
    content = re.sub(r'\.social-link:hover \.cmd-symbol \{[^}]*\}', '', content)
    
    # Add new terminal CSS before the closing </style> tag
    content = content.replace('</style>', TERMINAL_CSS + '\n    </style>')
    
    # Update existing CSS classes
    content = re.sub(
        r'\.social-links-grid \{[^}]*\}',
        '',
        content
    )
    
    content = re.sub(
        r'\.social-link \{[^}]*\}',
        '',
        content
    )
    
    content = re.sub(
        r'\.social-link:hover \{[^}]*\}',
        '',
        content
    )
    
    content = re.sub(
        r'\.footer-info \{[^}]*\}',
        '',
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
    
    print("\n✓ All pages updated with modern terminal-style footer!")

if __name__ == "__main__":
    main()
