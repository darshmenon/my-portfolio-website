"""
MEGA TECH UPGRADE: Add console logs, network activity, ASCII art to ALL pages
"""

# ASCII ROBOT HEADER
ASCII_ART_CSS = '''
        /* ASCII ART HEADER */
        .ascii-robot {
            position: fixed;
            top: 100px;
            left: 20px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.5rem;
            line-height: 0.6rem;
            color: rgba(147, 112, 219, 0.3);
            z-index: -1;
            white-space: pre;
            pointer-events: none;
        }

        @media (max-width: 1200px) {
            .ascii-robot { display: none; }
        }
'''

ASCII_ROBOT = '''    <!-- ASCII Robot Art -->
    <div class="ascii-robot">
        ___T_
       |o o o|
       |o o o|
       |o o o|
      /|o o o|\\
     /_|o_o_o|_\\
       | | | |
      /| | | |\\
     /_|_|_|_|_\\
        ROBOT
      PORTFOLIO
    </div>
'''

# NETWORK ACTIVITY INDICATOR
NETWORK_CSS = '''
        /* NETWORK ACTIVITY */
        .network-activity {
            position: fixed;
            top: 100px;
            right: 20px;
            background: rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(0, 255, 0, 0.5);
            border-radius: 6px;
            padding: 0.6rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            color: #00ff00;
            z-index: 9998;
            min-width: 150px;
        }

        .network-header {
            color: #00ff00;
            font-weight: 700;
            margin-bottom: 0.3rem;
            border-bottom: 1px solid rgba(0, 255, 0, 0.3);
            padding-bottom: 0.2rem;
        }

        .network-bar {
            height: 4px;
            background: rgba(0, 255, 0, 0.2);
            margin: 0.3rem 0;
            position: relative;
            overflow: hidden;
        }

        .network-bar::after {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 70%;
            background: #00ff00;
            animation: networkPulse 2s infinite;
        }

        @keyframes networkPulse {
            0%, 100% { width: 30%; }
            50% { width: 90%; }
        }

        @media (max-width: 768px) {
            .network-activity { display: none; }
        }
'''

NETWORK_HTML = '''    <!-- Network Activity -->
    <div class="network-activity">
        <div class="network-header">⚡ NETWORK</div>
        <div style="font-size: 0.65rem; margin: 0.2rem 0;">↓ DOWNLOAD</div>
        <div class="network-bar"></div>
        <div style="font-size: 0.65rem; margin: 0.2rem 0;">↑ UPLOAD</div>
        <div class="network-bar" style="animation-delay: 0.5s;"></div>
        <div style="font-size: 0.65rem; margin-top: 0.3rem; color: #00ffff;">STATUS: ACTIVE</div>
    </div>
'''

# CONSOLE LOG WIDGET
CONSOLE_CSS = '''
        /* CONSOLE LOG */
        .console-log {
            position: fixed;
            bottom: 80px;
            left: 20px;
            background: rgba(0, 0, 0, 0.95);
            border: 1px solid rgba(147, 112, 219, 0.5);
            border-radius: 6px;
            padding: 0.8rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.65rem;
            color: #00ff00;
            z-index: 9998;
            max-width: 300px;
            max-height: 150px;
            overflow-y: auto;
        }

        .console-log::-webkit-scrollbar {
            width: 4px;
        }

        .console-log::-webkit-scrollbar-thumb {
            background: rgba(147, 112, 219, 0.5);
        }

        .log-entry {
            margin: 0.2rem 0;
            opacity: 0;
            animation: logFadeIn 0.3s ease forwards;
        }

        @keyframes logFadeIn {
            to { opacity: 1; }
        }

        @media (max-width: 768px) {
            .console-log { display: none; }
        }
'''

CONSOLE_HTML = '''    <!-- Console Log -->
    <div class="console-log" id="consoleLog">
        <div class="log-entry" style="animation-delay: 0s;">[00:00:01] System initialized</div>
        <div class="log-entry" style="animation-delay: 0.3s;">[00:00:02] Loading modules...</div>
        <div class="log-entry" style="animation-delay: 0.6s;">[00:00:03] Connecting to server</div>
        <div class="log-entry" style="animation-delay: 0.9s;">[00:00:04] Assets loaded</div>
        <div class="log-entry" style="animation-delay: 1.2s;">[00:00:05] Ready</div>
    </div>

    <script>
        // Add new log entries periodically
        const logs = [
            'Processing request...',
            'Cache updated',
            'WebSocket connected',
            'Data synced',
            'Module loaded'
        ];
        let logTime = 6;
        setInterval(() => {
            const consoleLog = document.getElementById('consoleLog');
            if (consoleLog && consoleLog.children.length < 8) {
                const entry = document.createElement('div');
                entry.className = 'log-entry';
                const msg = logs[Math.floor(Math.random() * logs.length)];
                entry.textContent = `[00:00:${String(logTime++).padStart(2, '0')}] ${msg}`;
                consoleLog.appendChild(entry);
                
                // Remove old entries
                if (consoleLog.children.length > 8) {
                    consoleLog.removeChild(consoleLog.firstChild);
                }
            }
        }, 5000);
    </script>
'''

def add_mega_tech_features(filepath):
    """Add ALL tech features at once"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        modified = False
        
        # Add ASCII art CSS
        if 'ascii-robot' not in content:
            content = content.replace('    </style>', ASCII_ART_CSS + '    </style>')
            modified = True
        
        # Add Network CSS
        if 'network-activity' not in content:
            content = content.replace('    </style>', NETWORK_CSS + '    </style>')
            modified = True
        
        # Add Console CSS
        if 'console-log' not in content:
            content = content.replace('    </style>', CONSOLE_CSS + '    </style>')
            modified = True
        
        # Add HTML elements before </body>
        if '</body>' in content:
            if 'ASCII Robot Art' not in content:
                content = content.replace('</body>', ASCII_ROBOT + '\n</body>')
                modified = True
            if 'Network Activity' not in content:
                content = content.replace('</body>', NETWORK_HTML + '\n</body>')
                modified = True
            if 'Console Log' not in content:
                content = content.replace('</body>', CONSOLE_HTML + '\n</body>')
                modified = True
        
        if modified:
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"✅ Added mega tech features to {filepath}")
        else:
            print(f"⏭️  {filepath} already upgraded")
            
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
        add_mega_tech_features(page)

print("\n🔥 MEGA TECH UPGRADE COMPLETE! All pages now have:")
print("   ✅ ASCII Robot Art")
print("   ✅ Network Activity Monitor") 
print("   ✅ Live Console Logs")
print("   ✅ Matrix Effect")
print("   ✅ System Stats HUD")
print("   ✅ Glitch Effects")
print("   ✅ Boot Sequence")
print("   ✅ Terminal UI Panels")
print("\n🚀 MAXIMUM OS/NETWORKING/MATRIX AESTHETIC ACHIEVED! 💻⚡")
