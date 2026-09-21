import urllib.request
import os

urls = {
    'Apple': 'https://github.com/samuelngs/apple-emoji-ttf/raw/master/AppleColorEmoji.ttf',
    'Twemoji': 'https://github.com/mozilla/twemoji-colr/raw/master/TwemojiMozilla.ttf'
}

for name, url in urls.items():
    print(f'Downloading {name}...')
    try:
        filename = f'{name}.ttf'
        urllib.request.urlretrieve(url, filename)
        size_mb = os.path.getsize(filename) / 1024 / 1024
        print(f'{name} downloaded! Size: {size_mb:.2f} MB')
    except Exception as e:
        print(f'Failed to download {name}: {e}')
