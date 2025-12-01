"""
Apply UI panels to ALL remaining pages and add MORE techy elements
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
    """Add UI panel CSS before </style> tag if not already present"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check if already has UI panel CSS
        if 'ui-panel' in content and '.ui-dot:nth-child(1)' in content:
            print(f"⏭️  Skipped {filepath} (already has UI panels)")
            return
        
        # Add CSS before </style>
        content = content.replace('    </style>', UI_PANEL_CSS + '    </style>')
        
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✅ Added UI panel CSS to {filepath}")
    except Exception as e:
        print(f"❌ Error with {filepath}: {e}")

# Apply to remaining pages
pages = [
    '/Users/csureshkumar/my-portfolio-website/about/index.html',
    '/Users/csureshkumar/my-portfolio-website/robocloud-hub/index.html',
]

for page in pages:
    add_ui_panel_css(page)

print("\n🚀 UI panel CSS applied to all remaining pages!")
