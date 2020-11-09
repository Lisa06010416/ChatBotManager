import telegram
import requests
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler

class TelegramManager:
    def __init__(self, token):
        self.TELEGRAM_TOKEN = token
        self.telegram_bot = telegram.Bot(token)
        self.dispatcher = Dispatcher(self.telegram_bot, None)

    def set_webhook(self, url):
        # set weburl
        webhook_url = url + "/" + self.TELEGRAM_TOKEN + "/Telegram/webhook/"
        url = r"https://api.telegram.org/bot{token}/setWebhook?url={webhook_url}".format(token=self.TELEGRAM_TOKEN,
                                                                                         webhook_url=webhook_url)
        requests.get(url)




# 週期性提醒
# 爬蟲 and 分析 外幣
# 股票
# 資訊正負面
# 文字雲
# 預測模型