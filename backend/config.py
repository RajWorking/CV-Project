import os

FLASK_ENV = os.getenv('FLASK_ENV', 'development')
FLASK_DEBUG = os.getenv('FLASK_DEBUG', '1') == '1'
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "secret")

IMG_ROWS, IMG_COLS = 256, 256
EPSILON = 1e-8

