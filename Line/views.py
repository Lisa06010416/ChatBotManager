from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from dotenv import load_dotenv
import os
from chatbot.linebot.demo_manager import demoManager


# !! dotenv 不能再setting中使用，setting可以拿到
# !! 但是其他檔案沒有辦法用 from django.config import setting
# !! 來拿到setting中的值
# !! from django.config import setting 只能夠拿到靜態一開始就寫好的變數

# get secret
load_dotenv()
myUserId = os.getenv('myUserId')
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
# set line manager
lineManager = demoManager(myUserId, LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET)


# callback function to reply user message
@csrf_exempt
def line_callback(request):
    lineManager.callBack(request)
    return HttpResponse()


# push message to a user
def line_push_message(request):
    lineManager.linePushMessage({'text': 'send message to me'}, userID=lineManager.getMyUserID())
    return HttpResponse()


# broadcast message to users
def line_broadcast(request):
    lineManager.linePushMessage({'text': 'broadcast message'}, isBroadCast=True)
    return HttpResponse()