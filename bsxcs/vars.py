# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', False))
    MULTI_TOK1 = str(getenv('MULTI_TOK1', None))
    MULTI_TOK2 = str(getenv('MULTI_TOK2', None))
    MULTI_TOK3 = str(getenv('MULTI_TOK3', None))
    MULTI_TOK4 = str(getenv('MULTI_TOK4', None))
    API_ID = int(getenv('API_ID'))
    API_HASH = str(getenv('API_HASH'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5141332753:AAEDDqUiLe0PECzfe1V-tUOpILvssNP75_w'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60')) # 1 minte
    WORKERS = int(getenv('WORKERS', '6')) # 6 workers = 6 commands at once
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', None)) # you NEED to use a CHANNEL when you're using MULTI_CLIENT  
    PORT = int(getenv('PORT', 8080))
    BIND_ADDRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '1200')) # 20 minutes
    HAS_SSL = getenv('HAS_SSL', False)
    HAS_SSL = True if str(HAS_SSL).lower() == 'true' else False
    NO_PORT = getenv('NO_PORT', False)
    NO_PORT = True if str(NO_PORT).lower() == 'true' else False
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADDRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME + '.herokuapp.com'
    if ON_HEROKU:
        URL = f"https://{FQDN}/"     
    else:
        URL = "http{}://{}{}/".format('s' if HAS_SSL else '', FQDN, '' if NO_PORT else ':' + str(PORT))
