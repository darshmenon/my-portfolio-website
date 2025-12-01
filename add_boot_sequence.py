"""
Add TERMINAL BOOT SEQUENCE on page load - OS-style loading screen!
"""

BOOT_CSS = '''
        /* BOOT SEQUENCE OVERLAY */
        .boot-sequence {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #000;
            z-index: 99999;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            padding: 3rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            color: #00ff00;
            animation: fadeOut 0.5s ease 3s forwards;
            pointer-events: none;
        }

        .boot-line {
            opacity: 0;
            animation: bootLine 0.1s ease forwards;
        }

        @keyframes bootLine {
            to { opacity: 1; }
        }

        @keyframes fadeOut {
            to { opacity: 0; visibility: hidden; }
        }

        .boot-sequence .status-ok { color: #00ff00; }
        .boot-sequence .status-info { color: #00ffff; }
        .boot-sequence .status-warn { color: #ffaa00; }
'''

BOOT_HTML = '''    <!-- Boot Sequence -->
    <div class="boot-sequence" id="bootSequence">
        <div class="boot-line" style="animation-delay: 0s;">[ <span class="status-ok">OK</span> ] Starting DARSH_OS v2.0...</div>
        <div class="boot-line" style="animation-delay: 0.3s;">[ <span class="status-ok">OK</span> ] Loading kernel modules...</div>
        <div class="boot-line" style="animation-delay: 0.6s;">[ <span class="status-ok">OK</span> ] Initializing ROS2 environment...</div>
        <div class="boot-line" style="animation-delay: 0.9s;">[ <span class="status-ok">OK</span> ] Mounting robotics frameworks...</div>
        <div class="boot-line" style="animation-delay: 1.2s;">[ <span class="status-info">INFO</span> ] Connecting to neural network...</div>
        <div class="boot-line" style="animation-delay: 1.5s;">[ <span class="status-ok">OK</span> ] AI systems online</div>
        <div class="boot-line" style="animation-delay: 1.8s;">[ <span class="status-ok">OK</span> ] Portfolio interface ready</div>
        <div class="boot-line" style="animation-delay: 2.1s;">[ <span class="status-info">INFO</span> ] Welcome, visitor...</div>
    </div>
'''

def add_boot_sequence(filepath):
    """Add boot sequence"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        if 'boot-sequence' in content:
            print(f"⏭️  Skipped {filepath} (already has boot)")
            return
        
        content = content.replace('    </style>', BOOT_CSS + '    </style>')
        
        # Add after <body> tag
        if '<body>' in content and 'Boot Sequence' not in content:
            content = content.replace('<body>', '<body>\n' + BOOT_HTML)
        
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✅ Added boot sequence to {filepath}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

import os
pages = [
    '/Users/csureshkumar/my-portfolio-website/index.html',
    '/Users/csureshkumar/my-portfolio-website/about/index.html',
    '/Users/csureshkumar/my-portfolio-website/projects/index.html',
]

for page in pages:
    if os.path.exists(page):
        add_boot_sequence(page)

print("\n🚀 Boot sequence added to main pages! OS-style loading! 💾")
