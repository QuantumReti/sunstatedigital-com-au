from pathlib import Path
import shutil

root = Path(r'C:\Users\Josh\.openclaw\workspace\sunstatedigital-com-au')

mapping = {
    'index.html': '/',
    'about.html': '/about',
    'automation.html': '/automation',
    'contact.html': '/contact',
    'get-started.html': '/get-started',
    'google-ads.html': '/google-ads',
    'pricing.html': '/pricing',
    'privacy.html': '/privacy',
    'seo.html': '/seo',
    'social-media.html': '/social-media',
    'thankyou.html': '/thankyou',
    'website.html': '/website',
    'order.html': '/grow-your-business',
}

# Create clean-route folders with index.html copies
for src_name, route in mapping.items():
    if route == '/':
        continue
    src = root / src_name
    dest_dir = root / route.strip('/')
    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest_dir / 'index.html')

replacements = [
    ('/index.html', '/'),
    ('https://sunstatedigital.com.au/index.html', 'https://sunstatedigital.com.au/'),
    ('/about.html', '/about'),
    ('https://sunstatedigital.com.au/about.html', 'https://sunstatedigital.com.au/about'),
    ('/automation.html', '/automation'),
    ('https://sunstatedigital.com.au/automation.html', 'https://sunstatedigital.com.au/automation'),
    ('/contact.html', '/contact'),
    ('https://sunstatedigital.com.au/contact.html', 'https://sunstatedigital.com.au/contact'),
    ('/get-started.html', '/get-started'),
    ('https://sunstatedigital.com.au/get-started.html', 'https://sunstatedigital.com.au/get-started'),
    ('/google-ads.html', '/google-ads'),
    ('https://sunstatedigital.com.au/google-ads.html', 'https://sunstatedigital.com.au/google-ads'),
    ('/pricing.html', '/pricing'),
    ('https://sunstatedigital.com.au/pricing.html', 'https://sunstatedigital.com.au/pricing'),
    ('/privacy.html', '/privacy'),
    ('https://sunstatedigital.com.au/privacy.html', 'https://sunstatedigital.com.au/privacy'),
    ('/seo.html', '/seo'),
    ('https://sunstatedigital.com.au/seo.html', 'https://sunstatedigital.com.au/seo'),
    ('/social-media.html', '/social-media'),
    ('https://sunstatedigital.com.au/social-media.html', 'https://sunstatedigital.com.au/social-media'),
    ('/thankyou.html', '/thankyou'),
    ('https://sunstatedigital.com.au/thankyou.html', 'https://sunstatedigital.com.au/thankyou'),
    ('/website.html', '/website'),
    ('https://sunstatedigital.com.au/website.html', 'https://sunstatedigital.com.au/website'),
    ('/order.html', '/grow-your-business'),
    ('https://sunstatedigital.com.au/order.html', 'https://sunstatedigital.com.au/grow-your-business'),
]

html_files = list(root.glob('*.html')) + list(root.glob('*/*.html'))
for path in html_files:
    text = path.read_text(encoding='utf-8', errors='ignore')
    original = text
    for old, new in replacements:
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding='utf-8')
        print('UPDATED', path.relative_to(root))

print('DONE')
