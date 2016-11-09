import json
from channels import Group
from .models import Chat
from django.http import HttpResponse
from channels.handler import AsgiHandler
from .models import Chat

# def http_consumer(message):
#     # Make standard HTTP response - access ASGI path attribute directly
#     response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
#     # Encode that response into message format (ASGI)
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)
from .models import Chat
from django.contrib.auth.models import User

def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)


def ws_message(message):
    data = json.loads(message['text'])
    user = User.objects.get(username=data['user'])
    Chat.objects.create(from_user=user, message=data['msg'])
    # message.reply_channel.send({
    #     "text": message.content['text'],
    # })

def connect_chathome(message):
    print("connected")
    Group("new_chat").add(message.reply_channel)


def disconnect_chathome(message):
    Group("new_chat").discard(message.reply_channel)



