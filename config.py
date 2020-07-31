import os

BOT_NAME = os.environ.get("avisadius_bot", "")
CSE_KEY = os.environ.get("AIzaSyDtASgnIRAWYZIoxefihuH2rgriJ1nFErM", "")
CSE_CX = os.environ.get("013922059191334204857:gr8msb3oyls", "")
API_TOKEN = os.environ.get("1370044208:AAHpGzvGzxcJLJ6cF87w6RyQuYL3mllQfWo", "")
WEBHOOK_URL = os.environ.get("https://avisadius.herokuapp.com", "")
NGINX_SUBPATH = os.environ.get("NGINX_SUBPATH", "")
BATCH = int(os.environ.get("BATCH", 10))
POLLING = bool(os.environ.get("POLLING", False))

