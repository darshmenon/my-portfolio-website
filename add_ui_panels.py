"""
Script to add UI panel CSS to projects and blog pages for tech-geek aesthetic
"""

import re

# UI Panel CSS to add
UI_PANEL_CSS = '''        /* UI PANEL STYLES */
        .ui-panel {
            background: rgba(13, 2, 33, 0.7);
            border: 1px solid rgba(147, 112, 219, 0.5);
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 4rem;
            box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(20px);
            position: relative;
        }

        .ui-panel-header {
            background: rgba(147, 112, 219, 0.15);
            padding: 0.8rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(147, 112, 219, 0.3);
        }

        .ui-title {
            font-family: 'JetBrains Mono', monospace !important;
            color: #da70d6;
            font-weight: 700;
            font-size: 1.1rem;
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .ui-title::before {
            content: '>';
            color: #9370db;
            animation: blink 1.5s infinite;
        }

        .ui-controls {
            display: flex;
            gap: 8px;
        }

        .ui-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: rgba(147, 112, 219, 0.3);
        }

        .ui-dot:nth-child(1) {
            background: #ff5f56;
        }

        .ui-dot:nth-child(2) {
            background: #ffbd2e;
        }

        .ui-dot:nth-child(3) {
            background: #27c93f;
        }

        .ui-content {
            padding: 3rem;
            position: relative;
        }
'''

def add_ui_panel_css(filepath):
    """Add UI panel CSS before </style> tag"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Add CSS before </style>
    content = content.replace('    </style>', UI_PANEL_CSS + '    </style>')
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✅ Added UI panel CSS to {filepath}")

# Apply to projects and blog
add_ui_panel_css('/Users/csureshkumar/my-portfolio-website/projects/index.html')
add_ui_panel_css('/Users/csureshkumar/my-portfolio-website/blog/index.html')

print("\n✅ UI panel CSS added to all pages!")
