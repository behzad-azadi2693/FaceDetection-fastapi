from pathlib import Path
import os


BASE_DIR = Path('__file__').parent.parent


try:
    os.mkdir(os.path.join(BASE_DIR, 'media'))
    print('directory for save manage is created')
except:
    print('directory is exits')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
