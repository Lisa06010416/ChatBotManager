from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from chatBot.lineBot.manager.demoManager import demoManager

# ----to do----
# modify name
# dotenv

# init line manager
lineManager = demoManager()

# test
def getLinePage(request):
    return render(request, 'test.html', {})

# callback function to reply user message
@csrf_exempt #!!!
def lineCallBack(request):
    lineManager.callBack(request)
    return render()

# push message to a user
def linePushMessage(request):
    lineManager.linePushMessage({'text':'send message to me'}, userID=lineManager.getMyUserID())
    return HttpResponse()

# broadcast message to users
def lineBroadCast(request):
    lineManager.linePushMessage({'text': 'broadcast message'}, isBroadCast=True)
    return HttpResponse()


