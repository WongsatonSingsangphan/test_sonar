from threading import Event
import pandas as pd
import webbrowser
from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    TemplateSendMessage, ConfirmTemplate, MessageAction)
from openpyxl import load_workbook
import os
from linebot.models import (MessageEvent,TextMessage,FlexSendMessage,BubbleContainer,BoxComponent,TextComponent,ImageCarouselColumn,
BubbleStyle,BlockStyle,CarouselContainer,ImageComponent,MessageAction,ButtonComponent,ImageCarouselTemplate,URIAction,LocationAction,)
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
    #print(events)
    #BLOG https://www.tracthai.com/blog/

    if text == 'A':
        img_url_1 = 'https://clipground.com/images/1024x1024-png-14.png'
        img_url_2 = 'https://clipground.com/images/1024x1024-png-14.png'
        img_url_3 = 'https://clipground.com/images/1024x1024-png-14.png'
        img_url_4 = 'https://clipground.com/images/1024x1024-png-14.png'

        # กำหนดได้ไม่เกิน 10 อัน
        image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url=img_url_1,action=
                MessageAction(label='รายละเอียด',text='สินค้าที่1')),
            ImageCarouselColumn(image_url=img_url_2,action=
                MessageAction(label='รายละเอียด',text='สินค้าที่1')),
            ImageCarouselColumn(image_url=img_url_3,action=
                MessageAction(label='รายละเอียด',text='สินค้าที่1')),
            ImageCarouselColumn(image_url=img_url_4,action=
                MessageAction(label='รายละเอียด',text='สินค้าที่1')),
            ImageCarouselColumn(image_url=img_url_3,action=
                MessageAction(label='รายละเอียด',text='สินค้าที่1')),
            ImageCarouselColumn(image_url=img_url_3,action=
                MessageAction(label='รายละเอียด',text='สินค้าที่1')),
            ImageCarouselColumn(image_url=img_url_3,action=
                MessageAction(label='รายละเอียด',text='สินค้าที่1')),
            ImageCarouselColumn(image_url=img_url_3,action=
                MessageAction(label='รายละเอียด',text='สินค้าที่1')),
            ImageCarouselColumn(image_url=img_url_3,action=
                MessageAction(label='รายละเอียด',text='สินค้าที่1')),
            ImageCarouselColumn(image_url=img_url_3,action=
                MessageAction(label='รายละเอียด',text='สินค้าที่1'))
                ])
        
        template_message = TemplateSendMessage(alt_text='Hello',
                                               template=image_carousel_template)
        line_bot_api.reply_message(events.reply_token, template_message)

    if text == 'บริการ': # มีข้อความเดียว
        flex1 = BubbleContainer(
            size = 'mega', 
            hero = BoxComponent(
                layout='vertical',
                contents=[ImageComponent(url='https://clipground.com/images/1024x1024-png-14.png',
                                         size='full',
                                         action=MessageAction(
                                            label='รายละเอียด',
                                            text='ขอราคา'
                                        )
                                         )])) 
        
        flex2 = BubbleContainer(
            size = 'mega', 
            hero = BoxComponent(
                layout='vertical',
                contents=[ImageComponent(url='https://clipground.com/images/1024x1024-png-14.png',
                                         size='full',
                                         action=MessageAction(
                                            label='รายละเอียด',
                                            text='สถานนะส่งสินค้า'
                                        )
                                         )])) 
        carousel = CarouselContainer(contents=[flex1,flex2]) # max=12อัน
            
        flex_message = FlexSendMessage(alt_text='Hello',contents=carousel)
        line_bot_api.reply_message(events.reply_token,flex_message)

    if text == 'แจ้งปัญหา': # มี 1 ข้อความ และ มี 2 ปุ่ม primary แนวตั้ง URIAction
        flex = BubbleContainer(
            size = 'giga', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#ffffff')),
            body = BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='เลือกปัญหาที่ต้องการแจ้ง',
                                        align='center', # *start,end,center
                                        color='#000000',
                                        weight='regular', # *regular,bold
                                        style='normal', # *normal, italic
                                        decoration='none', # *none,underline,line-through
                                        size='md' # xxs,xs,sm,*md,lg,xl,xxl,3xl,4xl,5xl
                                        ),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#2acaea',
                                          margin = 'xs',
                                          action=MessageAction(
                                              label='ปัญหาที่1',
                                              text='ปัญหาที่1')),
                          ButtonComponent(style='secondary', # primary,secondary,link
                                          color='#ff494d',
                                          margin = 'xs',
                                          action=MessageAction(
                                              label='ปัญหาที่2',
                                              text='ปัญหาที่2')),
                          ButtonComponent(style='link', # primary,secondary,link
                                          color='#ffc181',
                                          margin = 'xs',
                                          action=MessageAction(
                                              label='กดแล้วได้ข้อความ',
                                              text='สวัสดีวันจันทร์'))]))     
           
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(events.reply_token,flex_message)

if __name__ == "__main__":
    app.run()