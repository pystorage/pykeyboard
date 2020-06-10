from .config import (SESSION_NAME, API_ID, API_HASH,
                     BOT_TOKEN, APP_PLUGINS)
from pyrogram import Client


class App(Client):
    def __init__(self):
        super().__init__(
            session_name=SESSION_NAME,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root=APP_PLUGINS)
        )

    def start(self, *args):
        super().start()

    def stop(self, *args):
        super().stop()
