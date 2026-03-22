
from pyrogram import client, __version__
from info import API_ID, API_HASH, BOT_TOKEN, PORT
from utils import temp
from aiohttp import web
from web.route import web_server
from config_manager import init_config


class Bot(client):

    def __init__(self):
        super().__init__(
            name="FileToLinkBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        init_config()
        await super().start()
        temp.BOT = self
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()
        print(f"Bot started. Pyrogram v{__version__}")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")
    
app = Bot()
app.run()
