import logging
from login import client
from telethon.tl.functions.account import UpdateStatusRequest
import time
from data import delay

if client.is_user_authorized():
    logging.info("You are now AlwaysOnline™, Yah!")
    while True:
        client(UpdateStatusRequest(offline=False))
        time.sleep(delay)
        logging.debug("Sleep for 1 min")
else:
    logging.fatal("Login Fails, please retry...")
