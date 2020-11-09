from linebot.models import MessageEvent, TextSendMessage

from chatbot.linebot.manager.line_manager import lineManager


class demoManager(lineManager):
    def __init__(self, myuserId, access_token, channel_secret):
        lineManager.__init__(self, myuserId, access_token, channel_secret)

    def _callback_method(self, line_bot_api, events):
        for event in events:
            if isinstance(event, MessageEvent):
                line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=event.message.text)
                        )

    def _push_message_method(self, line_bot_api, message_dic, userid_set):
        line_bot_api.push_message(userid_set, TextSendMessage(text=message_dic['text']))

    def _broadcast_message_method(self, line_bot_api, message_dic):
        line_bot_api.broadcast(TextSendMessage(text=message_dic['text']))
