"""
Add Matrix-style code rain effect to all pages for ULTIMATE tech aesthetic
"""

MATRIX_CSS = '''
        /* MATRIX CODE RAIN EFFECT */
        .matrix-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -3;
            opacity: 0.05;
            pointer-events: none;
        }
'''

MATRIX_HTML = '''    <!-- Matrix Code Rain Background -->
    <canvas class="matrix-canvas" id="matrixCanvas"></canvas>

    <script>
        // Matrix Code Rain Effect
        const canvas = document.getElementById('matrixCanvas');
        if (canvas) {
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            const chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
            const fontSize = 14;
            const columns = canvas.width / fontSize;
            const drops = Array(Math.floor(columns)).fill(1);

            function drawMatrix() {
                ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = '#9370db';
                ctx.font = fontSize + 'px JetBrains Mono';

                for (let i = 0; i < drops.length; i++) {
                    const text = chars[Math.floor(Math.random() * chars.length)];
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                    if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                        drops[i] = 0;
                    }
                    drops[i]++;
                }
            }

            setInterval(drawMatrix, 50);

            window.addEventListener('resize', () => {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            });
        }
    </script>
'''

def add_matrix_effect(filepath):
    """Add Matrix code rain effect"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check if already has matrix effect
        if 'matrixCanvas' in content:
            print(f"⏭️  Skipped {filepath} (already has matrix effect)")
            return
        
        # Add CSS before </style>
        if '    </style>' in content and 'MATRIX CODE RAIN' not in content:
            content = content.replace('    </style>', MATRIX_CSS + '    </style>')
        
        # Add canvas and script after <body>
        if '<body>' in content and 'Matrix Code Rain Background' not in content:
            content = content.replace('<body>', '<body>\n' + MATRIX_HTML)
        
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✅ Added Matrix effect to {filepath}")
            
    except Exception as e:
        print(f"❌ Error with {filepath}: {e}")

# Apply to all pages
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
        add_matrix_effect(page)

print("\n🟢 Matrix code rain effect added to ALL pages! Neo would be proud! 🕶️")
