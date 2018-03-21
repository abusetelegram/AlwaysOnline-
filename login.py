from telethon import TelegramClient
from data import *
import logging
import getpass

logging.basicConfig(level=logging.DEBUG)
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
if api_id == '' or api_hash == '':
    logging.fatal("You must assign a API before using this script!")

logging.info("Trying to Login to Telegram...")
client = TelegramClient('session_file', api_id, api_hash, update_workers=1, spawn_read_thread=False)

if client.connect() is not True:
    logging.info('You have not login yet, Trying to log you in...')
    logging.info('if you have 2FA password, please enter right now. This Password will not be stored: ')
    password = getpass.getpass()
    if password != '':
        client.start(password=password)
    else:
        client.start()
