from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 20173337))
    API_HASH = env.get("TELEGRAM_API_HASH", "f672963099862a8a20a5f7dfe27f4b56")
    OWNER_ID = int(env.get("OWNER_ID", 6667876837))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Direct_Dl_Linux_Bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6477692662:AAH3Mag1sGpjntptYJLSu8QSPyEQhJnyeJI")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002072097127))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "linux-bots-5f9c0c9701d5.herokuapp.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
