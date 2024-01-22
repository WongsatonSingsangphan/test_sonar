from threading import Event
import pandas as pd
import webbrowser
from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,TextMessage,FlexSendMessage,BubbleContainer,BoxComponent,TextComponent,
BubbleStyle,BlockStyle,CarouselContainer,ImageComponent,MessageAction,ButtonComponent,URIAction,LocationAction,
SeparatorComponent)

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
    #print(events)
    #BLOG https://www.tracthai.com/blog/

channel_secret = "78e93310e943248a7a53639cb1b668b7"
channel_access_token = "0EB6kJ8Npso89qsPBaTFxrpYsvmE6ei7lvMr7KzdMHRxW4AQUUo9ucAF7oTONjPDppSNCViu5+r7frw6EsT+XCpbx9uet8iAElaGk3kr1BA8bXaUGPaVt+WbrKiDfk3EwDUhKR8HnvO6jHShB2DAygdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)

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
def handle_text_message(event):
    text = event.message.text
    print(text)  
  
    if text == "B":
        flex = BubbleContainer(
            header=BoxComponent(
                layout='vertical',
                background_color='#8f000a',
                contents=[TextComponent(
                    text='ข้อมูลผู้ใช้',
                    align='center',
                    color='#FFFFFF',
                    weight='bold',
                )]
            ),
            hero=ImageComponent(
                layout='vertical',
                url='https://scontent.fbkk9-3.fna.fbcdn.net/v/t31.18172-8/27368852_432967333788572_5497155771020619860_o.jpg?_nc_cat=105&ccb=1-7&_nc_sid=300f58&_nc_ohc=xDWHDChQDRMAX9lAmJ9&_nc_ht=scontent.fbkk9-3.fna&oh=00_AfBaQ7XjClbHwIvxeQo6lfJHyxAGVh6F2_hQGtPvHpsuQQ&oe=65A8B65A',
                size='xl',
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(
                        text='นายภูมิ ภานุสถิตย์',
                        size='xl',
                        weight='bold',
                        align='center',
                    ),
                    TextComponent(
                        text='นักสู้',
                        align='center',
                    ),
                    SeparatorComponent(
                        margin='md',
                    ),
                    BoxComponent(
                        layout='vertical',
                        contents=[
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "Visit our website",
                                    "uri": "https://www.facebook.com/profile.php?id=100012259268196",
                                },
                                "style": "link",
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "Register with us",
                                    "uri": "https://liff.line.me/xxxxx-xxxxx/",
                                },
                                "style": "link",
                            },
                        ],
                        paddingTop='10px',
                    ),
                ],
            ),
        )

        # สร้าง FlexSendMessage และส่งกลับให้กับ Line Bot
        flex_message = FlexSendMessage(alt_text='Hello', contents=flex)
        line_bot_api.reply_message(event.reply_token, flex_message)
        
if __name__ == "__main__":
    app.run()