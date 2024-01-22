import pandas as pd
from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    TemplateSendMessage, ConfirmTemplate, MessageAction)
from openpyxl import load_workbook
import os
from linebot.models import (MessageEvent,
                            TextMessage,
                            FlexSendMessage,
                            BubbleContainer,
                            BoxComponent,
                            TextComponent,
                            BubbleStyle,
                            BlockStyle,
                            CarouselContainer,
                            ImageComponent,
                            MessageAction,
                            ButtonComponent)
import os
import requests, urllib.parse

channel_secret = "78e93310e943248a7a53639cb1b668b7"
channel_access_token = "0EB6kJ8Npso89qsPBaTFxrpYsvmE6ei7lvMr7KzdMHRxW4AQUUo9ucAF7oTONjPDppSNCViu5+r7frw6EsT+XCpbx9uet8iAElaGk3kr1BA8bXaUGPaVt+WbrKiDfk3EwDUhKR8HnvO6jHShB2DAygdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)

@app.route("/", methods=["GET","POST"])
def home():
    try:
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        handler.handle(body, signature)
    except:
        pass
    
    return "Hello Line Chatbot"

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(events):
    usernumdic = eval(str(events.source))['userId']
    #latitude_text = eval(type(event.message))['latitude']
    text = events.message.text
    #print(str(event.message))
    print(usernumdic)
    print(text)
    print(events)

    if events.message.type == 'location':
        latitude = events.message.latitude
        print(f"Latitude: {latitude}")

if __name__ == "__main__":
    app.run()
   
