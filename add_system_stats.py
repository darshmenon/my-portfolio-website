"""
Add SYSTEM STATS DISPLAY to all pages - CPU/RAM/Network indicators like a real OS!
"""

SYSTEM_STATS_CSS = '''
        /* SYSTEM STATS HUD */
        .system-stats {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(147, 112, 219, 0.5);
            border-radius: 8px;
            padding: 0.8rem 1.2rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            color: #00ff00;
            z-index: 9999;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 20px rgba(147, 112, 219, 0.3);
            min-width: 200px;
        }

        .system-stats-header {
            color: #da70d6;
            font-weight: 700;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            border-bottom: 1px solid rgba(147, 112, 219, 0.3);
            padding-bottom: 0.3rem;
        }

        .stat-line {
            display: flex;
            justify-content: space-between;
            margin: 0.3rem 0;
            color: #00ff00;
        }

        .stat-label {
            color: #9370db;
        }

        .stat-value {
            color: #00ff00;
            font-weight: 700;
        }

        .status-indicator {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #00ff00;
            display: inline-block;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }

        @media (max-width: 768px) {
            .system-stats {
                display: none;
            }
        }
'''

SYSTEM_STATS_HTML = '''    <!-- System Stats HUD -->
    <div class="system-stats">
        <div class="system-stats-header">
            <span class="status-indicator"></span>
            SYSTEM_MONITOR
        </div>
        <div class="stat-line">
            <span class="stat-label">CPU:</span>
            <span class="stat-value" id="cpu-stat">23%</span>
        </div>
        <div class="stat-line">
            <span class="stat-label">RAM:</span>
            <span class="stat-value" id="ram-stat">4.2 GB</span>
        </div>
        <div class="stat-line">
            <span class="stat-label">NET:</span>
            <span class="stat-value" id="net-stat">↓ 2.4 MB/s</span>
        </div>
        <div class="stat-line">
            <span class="stat-label">UPTIME:</span>
            <span class="stat-value" id="uptime-stat">00:00</span>
        </div>
    </div>

    <script>
        // Animated system stats
        let startTime = Date.now();
        
        function updateStats() {
            // CPU (random between 15-35%)
            document.getElementById('cpu-stat').textContent = (Math.random() * 20 + 15).toFixed(1) + '%';
            
            // RAM (random between 3.8-5.2 GB)
            document.getElementById('ram-stat').textContent = (Math.random() * 1.4 + 3.8).toFixed(1) + ' GB';
            
            // Network (random speed)
            const speed = (Math.random() * 3 + 1).toFixed(1);
            document.getElementById('net-stat').textContent = '↓ ' + speed + ' MB/s';
            
            // Uptime
            const uptime = Math.floor((Date.now() - startTime) / 1000);
            const mins = Math.floor(uptime / 60);
            const secs = uptime % 60;
            document.getElementById('uptime-stat').textContent = 
                String(mins).padStart(2, '0') + ':' + String(secs).padStart(2, '0');
        }
        
        setInterval(updateStats, 1000);
        updateStats();
    </script>
'''

def add_system_stats(filepath):
    """Add system stats HUD"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check if already has system stats
        if 'SYSTEM_MONITOR' in content:
            print(f"⏭️  Skipped {filepath} (already has system stats)")
            return
        
        # Add CSS before </style>
        if '    </style>' in content:
            content = content.replace('    </style>', SYSTEM_STATS_CSS + '    </style>')
        
        # Add HTML before </body>
        if '</body>' in content:
            content = content.replace('</body>', SYSTEM_STATS_HTML + '\n</body>')
        
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✅ Added system stats to {filepath}")
            
    except Exception as e:
        print(f"❌ Error with {filepath}: {e}")

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
        add_system_stats(page)

print("\n📊 System stats HUD added to all pages! Like a real OS! 💻")
