#서버 환경

from config.default import *
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, '.env'))


SQLALCHEMY_DATABASE_URI = 'postgresql://dbmasteruser:7nw?m8a!CNWTHd)nwL{dODo5eS~Q@ls-73552afb2c0c9f23f45aa5b86375a4b2bcb4e31f.cnpd0ghscnrt.ap-northeast-2.rds.amaz>/flask_pybo2:5432'.format(
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME'))

SQLALCHEMY_TRACK_MODIFICATIONS = False
# SECRET_KEY = '7nw?m8a!CNWTHd)nwL{dODo5eS~Q'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})