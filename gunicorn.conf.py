from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STATIC_ROOT = BASE_DIR / 'static'

...

# Adicione esta linha para especificar a pasta static como um diret�rio est�tico
STATIC_DIRS = [STATIC_ROOT]

...
