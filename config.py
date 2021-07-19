import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
admins = [
    863325996
]
channels = [-1001543183452]
URL_MONOBANK = str(os.getenv('URL_MONOBANK'))
URL_DEVELOPER = str(os.getenv('URL_DEVELOPER'))
URL_LOC_SKV = str(os.getenv('URL_LOC_SKV'))
URL_SITE_SKV = str(os.getenv('URL_SITE_SKV'))
URL_LOC_VL = str(os.getenv('URL_LOC_VL'))
URL_SITE_VL = str(os.getenv('URL_SITE_VL'))
TOKEN_MONOBANK = str(os.getenv('TOKEN_MONOBANK'))
ip = os.getenv('ip')
QIWI_TOKEN = os.getenv('qiwi')
QIWI_PUBKEY = str(os.getenv('qiwi_p_pub'))
QIWI_SECRET = str(os.getenv('qiwi_secret'))
QIWI_WALLET = str(os.getenv('qiwi_wallet'))




aiogram_redis = {
    'host': ip,
}

redis = {
    'adress': (ip, 6379),
    'encoding': 'utf'
}

PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')


