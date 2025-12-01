"""
Add GLITCH EFFECT to page titles for cyberpunk aesthetic
"""

GLITCH_CSS = '''
        /* GLITCH EFFECT */
        .glitch {
            position: relative;
            animation: glitch-skew 1s infinite;
        }

        .glitch::before,
        .glitch::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .glitch::before {
            left: 2px;
            text-shadow: -2px 0 #ff00ff;
            clip: rect(44px, 450px, 56px, 0);
            animation: glitch-anim 5s infinite linear alternate-reverse;
        }

        .glitch::after {
            left: -2px;
            text-shadow: -2px 0 #00ffff, 2px 2px #ff00ff;
            clip: rect(44px, 450px, 56px, 0);
            animation: glitch-anim2 5s infinite linear alternate-reverse;
        }

        @keyframes glitch-anim {
            0% { clip: rect(31px, 9999px, 94px, 0); }
            20% { clip: rect(60px, 9999px, 73px, 0); }
            40% { clip: rect(10px, 9999px, 85px, 0); }
            60% { clip: rect(76px, 9999px, 11px, 0); }
            80% { clip: rect(93px, 9999px, 52px, 0); }
            100% { clip: rect(2px, 9999px, 61px, 0); }
        }

        @keyframes glitch-anim2 {
            0% { clip: rect(65px, 9999px, 100px, 0); }
            20% { clip: rect(52px, 9999px, 74px, 0); }
            40% { clip: rect(79px, 9999px, 85px, 0); }
            60% { clip: rect(2px, 9999px, 40px, 0); }
            80% { clip: rect(18px, 9999px, 83px, 0); }
            100% { clip: rect(44px, 9999px, 29px, 0); }
        }

        @keyframes glitch-skew {
            0% { transform: skew(0deg); }
            10% { transform: skew(-2deg); }
            20% { transform: skew(2deg); }
            30% { transform: skew(0deg); }
            100% { transform: skew(0deg); }
        }
'''

def add_glitch_effect(filepath):
    """Add glitch effect CSS"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        if 'glitch-skew' in content:
            print(f"⏭️  Skipped {filepath} (already has glitch)")
            return
        
        content = content.replace('    </style>', GLITCH_CSS + '    </style>')
        
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✅ Added glitch effect to {filepath}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

import os
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
        add_glitch_effect(page)

print("\n⚡ Glitch effect added! Cyberpunk aesthetic complete! 🌆")
