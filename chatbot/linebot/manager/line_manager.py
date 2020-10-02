import abc

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import LineBotApiError

class lineManager(abc.ABC):
    def __init__(self, myuserId, access_token, channel_secret):
        self.__myUserId = myuserId
        self.__line_bot_api = LineBotApi(access_token)
        self.__parser = WebhookParser(channel_secret)

    # get property
    def getMyUserID(self):
        return self.__myUserId

    def getLineBotAPI(self):
        return self.__line_bot_api

    def getParse(self):
        return self.__parser

    # reply message
    def callBack(self, request):
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        parser = self.getParse()
        events = parser.parse(body, signature)

        lineBotAPI = self.getLineBotAPI()
        self._callBackMethod(lineBotAPI, events)

    @abc.abstractmethod
    def _callBackMethod(self, lineBotAPI, events):
        return NotImplemented

    # push message contain push and broadcast
    def linePushMessage(self, messageDic, userID=None, isBroadCast=False):
        try:
            lineBotAPI = self.getLineBotAPI()
            if isBroadCast:
                self._broadcastMessageMethod(lineBotAPI, messageDic)
            else:
                self._pushMessageMethod(lineBotAPI, messageDic, userID)
        except LineBotApiError as e:
            raise e

    @abc.abstractmethod
    def _pushMessageMethod(self, lineBotAPI, messageDic, userIdSet):
        return NotImplemented

    @abc.abstractmethod
    def _broadcastMessageMethod(self, lineBotAPI, messageDic):
        return NotImplemented
