from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STATIC_ROOT = BASE_DIR / 'static'

...

# Adicione esta linha para especificar a pasta static como um diret�rio est�tico
STATICFILES_DIRS = [STATIC_ROOT]


...


workers = 4  # ajuste o número de trabalhadores aqui
worker_connections = 1000