import json
import os

import requests
import telegram
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

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

# https://hackmd.io/@BpUgvpG2TZy_PvDRF1bwvw/HkgaMUc24?type=view
#
def hello(bot, update):
    update.message.reply_text('hello, {}'.format(update.message.from_user.first_name))


def button(bot,update):
    update.message.reply_text('喵喵～',
                              reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('課程網站', url = 'https://github.com/mzshieh/pa19spring'),
            InlineKeyboardButton('Documentation', url = 'https://python-telegram-bot.readthedocs.io/en/stable/index.html')]]))


def a():
    return "123"


# New a dispatcher for bot
dispatcher = Dispatcher(telegram_bot, None)
# 順序重要!
# command hello
dispatcher.add_handler(CommandHandler('hello', hello))
# add a button to dispatcher
dispatcher.add_handler(CommandHandler('button', button))
#
# add a handler to dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))


print(dispatcher.handlers[0][0].command)
print(dispatcher.handlers[0][0].callback)
