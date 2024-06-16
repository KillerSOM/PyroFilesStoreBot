# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "22466557"))
	API_HASH = os.environ.get("API_HASH", "020e8aa708282ed9b5210d84ba374736")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "7136288796:AAH6CWn7TIVxR8F7TUxVlrkxRIiQI606NXk")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Sanji_Test_Robot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001957744474"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5297903100"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://killersom72:killersom72@sanjifilestore.x6rhkdi.mongodb.net/?retryWrites=true&w=majority&appName=SanjiFileStore")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001813852666")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @KillerSOM

👥 **Support Group:** [Linux Repositories](https://t.me/anime_zone_x1)

📢 **Updates Group:** [Discovery Projects](https://t.me/anime_zone_x1)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @KillerSOM

Developer is Super Noob. Just Learning from Official Docs. 

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.


"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
