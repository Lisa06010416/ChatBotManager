from linebot.models import MessageEvent, TextSendMessage

from chatbot.linebot.manager.line_manager import lineManager


class demoManager(lineManager):
    def __init__(self, myuserId, access_token, channel_secret):
        lineManager.__init__(self, myuserId, access_token, channel_secret)

    def _callBackMethod(self, lineBotAPI, events):
        for event in events:
            if isinstance(event, MessageEvent):
                lineBotAPI.reply_message(
                            event.reply_token,
                            TextSendMessage(text=event.message.text)
                        )

    def _pushMessageMethod(self, lineBotAPI, messageDic, userIdSet):
        lineBotAPI.push_message(userIdSet, TextSendMessage(text=messageDic['text']))

    def _broadcastMessageMethod(self, lineBotAPI, messageDic):
        lineBotAPI.broadcast(TextSendMessage(text=messageDic['text']))