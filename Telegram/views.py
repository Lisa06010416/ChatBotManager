import json
import os

import requests
import telegram
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from telegram.ext import Dispatcher, MessageHandler, Filters

# load telegram token
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
NGROK_URL = os.getenv('NGROK_URL')
# creat telegram bot
telegram_bot = telegram.Bot(TELEGRAM_TOKEN)
# set weburl
url = r"https://api.telegram.org/bot{token}/setWebhook?url={webhook_url}".format(token=TELEGRAM_TOKEN,
                                                                                 webhook_url=NGROK_URL + "/Telegram/webhook/")
response = requests.get(url)


@csrf_exempt
def webhook_handler(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        update = telegram.Update.de_json(data, telegram_bot)
        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return HttpResponse()


def reply_handler(bot, update):
    """Reply message."""
    text = update.message.text
    update.message.reply_text(text)


# New a dispatcher for bot
dispatcher = Dispatcher(telegram_bot, None)
# add a handler to dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))
