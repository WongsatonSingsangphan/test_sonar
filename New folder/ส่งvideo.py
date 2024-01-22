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
                            VideoSendMessage,
                            BlockStyle,
                            CarouselContainer,
                            ImageComponent,
                            MessageAction,
                            SeparatorComponent,
                            FillerComponent)
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
    if text == 'A': # มีครบ 4 ส่วน header, hero, body, footer
        flex = BubbleContainer(
            header = BoxComponent(layout='vertical',
                                  contents=[TextComponent(
                                      text='header',align='center')]),
            hero = BoxComponent(layout='vertical',
                                contents=[TextComponent(
                                    text='hero',align='center')]),
            body = BoxComponent(layout='vertical',
                                contents=[TextComponent(
                                    text='body',align='center')]),
            footer = BoxComponent(layout='vertical',
                                  contents=[TextComponent(
                                      text='footer',align='center')]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(events.reply_token,flex_message)

    if text == 'C':
        video_message = VideoSendMessage(
        original_content_url="https://i.ytimg.com/an_webp/gSuL7cBYZo8/mqdefault_6s.webp?du=3000&sqp=CNyVhawG&rs=AOn4CLCuwby6l3UNcuRAi36IvvFDs6dsFg",
        preview_image_url="https://i.ytimg.com/an_webp/gSuL7cBYZo8/mqdefault_6s.webp?du=3000&sqp=CNyVhawG&rs=AOn4CLCuwby6l3UNcuRAi36IvvFDs6dsFg"
        )
        line_bot_api.reply_message(events.reply_token, video_message)
        # สร้าง FlexSendMessage และส่งกลับให้กับ Line Bot
        #flex_message = FlexSendMessage(alt_text='Hello', contents=bubble_container)
        #line_bot_api.reply_message(events.reply_token, flex_message)


if __name__ == "__main__":
    app.run()
   
