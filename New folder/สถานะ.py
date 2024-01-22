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
        flex = BubbleContainer(
                size='mega',
                header=BoxComponent(
                layout='vertical',
                contents=[
                            TextComponent(
                                text='จาก',
                                color='#ffffff66',
                                size='sm'),
                            TextComponent(
                                text='นครปฐม',
                                color='#ffffff',
                                size='xl',
                                flex=4,
                                weight='bold'),
                            TextComponent(
                                text='ไป',
                                color='#ffffff66',
                                size='sm'),
                            TextComponent(
                                text='กทม',
                                color='#ffffff',
                                size='xl',
                                flex=4,
                                weight='bold')
                         ],
                padding_all='20px',
                background_color='#0367D3',
                spacing='md',
                height='154px',
                padding_top='22px'),
            body=BoxComponent(
                    layout='vertical',
                    contents=[
                    TextComponent(
                        text='Total: 1 hour',
                        color='#302f2f',
                        size='xs'),
                    BoxComponent(
                        layout='horizontal',
                        contents=[
                            TextComponent(
                                text='20:30',
                                size='sm',
                                gravity='center'),
                            BoxComponent(
                                layout='vertical',
                                contents=[
                                    FillerComponent(),
                                    BoxComponent(
                                        layout='vertical',
                                        contents=[],
                                        corner_radius='30px',
                                        height='12px',
                                        width='12px',
                                        border_color='#EF454D',
                                        border_width='2px'),
                                    FillerComponent()],
                                        flex=0),
                            TextComponent(
                                text='กทม',
                                gravity='center',
                                flex=4,
                                size='sm')],
                                spacing='lg',
                                corner_radius='30px',
                                margin='xl'),
                    BoxComponent(
                        layout='horizontal',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                contents=[FillerComponent()],
                                flex=1),]),
                            BoxComponent(
                                layout='vertical',
                                contents=[
                                    BoxComponent(
                                        layout='horizontal',
                                        contents=[
                                            FillerComponent(),
                                            BoxComponent(
                                                layout='vertical',
                                                contents=[],
                                                width='2px',
                                                background_color='#B7B7B7'),
                                            FillerComponent()],
                                                flex=1)],
                                                width='12px'),
                    TextComponent(
                        text='เดินทาง 10 นาที',
                        gravity='center',
                        flex=4,
                        size='xs',
                        color='#8c8c8c'),
                    SeparatorComponent(),
                    BoxComponent(
                        layout='horizontal',
                        contents=[
                            BoxComponent(
                                layout='horizontal',
                                contents=[
                                    TextComponent(
                                        text='20:34',
                                        gravity='center',
                                        size='sm')],
                                        flex=1),
                                        
                            BoxComponent(
                                layout='vertical',
                                contents=[
                                    FillerComponent(),
                                    BoxComponent(
                                        layout='vertical',
                                        contents=[],
                                        corner_radius='30px',
                                        width='12px',
                                        height='12px',
                                        border_width='2px',
                                        border_color='#6486E3'),
                                    FillerComponent()],
                                        flex=0
                                        ),
                                    TextComponent(
                                        text='กำลังเดินทาง',
                                        gravity='center',
                                        flex=4,
                                        size='sm')
                                    ],
                                    spacing='lg',
                                    corner_radius='30px'
                                    ),
                                    
                                    ],
                padding_all='20px',
                background_color='#ffffff',
                spacing='md',
                height='154px',
                padding_top='22px'),
        )

        # Assume event and line_bot_api are defined
        flex_message = FlexSendMessage(alt_text='Hello', contents=flex)
        line_bot_api.reply_message(events.reply_token, flex_message)

if __name__ == "__main__":
    app.run()
   
