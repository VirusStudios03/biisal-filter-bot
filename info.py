import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '22549633'))
API_HASH = environ.get('API_HASH', '34d8c9887fe445c1dac2228cbdf9ab48')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '2057170163 6835418766 7802198323').split()]
USERNAME = environ.get('USERNAME', "https://t.me/Filter_Bots_Support_Bot")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001995831309'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+K1NZBcq2mZ1lMzA1')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001850355982').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://V2Prime:PeEb6SAwboCfjD9K@mrvirus.ythkz.mongodb.net/?retryWrites=true&w=majority&appName=MrVirus")

DATABASE_NAME = environ.get('DATABASE_NAME', "MrVirus")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001995831309'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/571b4b689b6f0d8ab279e-e715961e20edeb0d61.jpg')
START_IMG = environ.get('START_IMG', 'https://graph.org/file/647d1e6bd00d45cff21e0-d7d9fac281143b464d.jpg https://graph.org/file/50db43d87e203f4b63238-e33bba9c2996d23a21.jpg https://graph.org/file/3e5e98a78417b7701b550-3ac486fdf6bb7eb340.jpg https://graph.org/file/4aa13337155a29b932ffd-7ab703a89aeeeca896.jpg https://graph.org/file/728cbbc0300b493498be2-ba910a5525ed992225.jpg https://graph.org/file/5d400388bd8b187c9cd1e-3087fb954f07febbe3.jpg https://graph.org/file/28fd50a92459df899e8ec-2b279a1e4af85dc54a.jpg').split()
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1001995831309'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1001995831309'))
URL = environ.get('URL', 'mytestbot-jvdfhbj.com')
STICKERS_IDS = ('CAACAgUAAxkBAAIq4GcLuVcGzLFjzmuLAim3O8SR7-QeAAJiFAACNUZgVGUa8UCdFTy-NAQ').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1001995831309'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Virus_Botz/52")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "390b93d6cc4c6843fdaa7db0eff92f8c3819dacb")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'instantearn.in')
SHORTENER_API2 = environ.get("SHORTENER_API2", "390b93d6cc4c6843fdaa7db0eff92f8c3819dacb")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'instantearn.in')
SHORTENER_API3 = environ.get("SHORTENER_API3", "390b93d6cc4c6843fdaa7db0eff92f8c3819dacb")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'instantearn.in')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "43200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "43200"))

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
auth_channel = environ.get('AUTH_CHANNEL', '-1002224811479')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002243830434'))
request_channel = environ.get('REQUEST_CHANNEL', '-1001995831309')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1001995831309'))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002224811479'))

AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
    }
DEFAULT_POST_MODE = {
    'singel_post_mode' : False,
    'all_files_post_mode' : False
}
