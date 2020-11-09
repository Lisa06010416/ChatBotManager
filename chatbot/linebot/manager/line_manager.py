import abc

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import LineBotApiError

class lineManager(abc.ABC):
    def __init__(self, myuserId, access_token, channel_secret):
        self.__myUserId = myuserId
        self.__line_bot_api = LineBotApi(access_token)
        self.__parser = WebhookParser(channel_secret)

    # get property
    def get_myuserid(self):
        return self.__myUserId

    def get_linebot_api(self):
        return self.__line_bot_api

    def get_parse(self):
        return self.__parser

    # reply message
    def callback(self, request):
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        parser = self.get_parse()
        events = parser.parse(body, signature)

        lineBotAPI = self.get_linebot_api()
        self._callback_method(lineBotAPI, events)

    @abc.abstractmethod
    def _callback_method(self, line_bot_api, events):
        return NotImplemented

    # push message contain push and broadcast
    def line_push_message(self, message_dic, userid=None, is_broadcast=False):
        try:
            lineBotAPI = self.get_linebot_api()
            if is_broadcast:
                self._broadcast_message_method(lineBotAPI, message_dic)
            else:
                self._push_message_method(lineBotAPI, message_dic, userid)
        except LineBotApiError as e:
            raise e

    @abc.abstractmethod
    def _push_message_method(self, line_bot_api, message_dic, userid_set):
        return NotImplemented

    @abc.abstractmethod
    def _broadcast_message_method(self, line_bot_api, message_dic):
        return NotImplemented
