from flask import Flask, request, send_from_directory
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,TextMessage,FlexSendMessage,BubbleContainer,BoxComponent,
                            TextComponent,TextSendMessage,MessageAction,BubbleStyle,
                            BlockStyle,LocationMessage,FlexSendMessage,BoxComponent,
                            BubbleStyle,BlockStyle,ButtonComponent,LocationAction, QuickReply, 
                            QuickReplyButton,URIAction,CameraRollAction,CameraAction,PostbackAction,
                            DatetimePickerAction)

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
    #user_ID = event.message.userId
    #print(user_ID)
    print(text)  
    
    if text == "B":
        flex = QuickReply(
                            items=[
                                QuickReplyButton(
                                    action=URIAction(label="URI", uri="https://developers.line.biz")
                                ),
                                QuickReplyButton(
                                    action=CameraRollAction(label="Camera Roll")
                                ),
                                QuickReplyButton(
                                    action=CameraAction(label="Camera")
                                ),
                                QuickReplyButton(
                                    action=LocationAction(label="Location")
                                ),
                                QuickReplyButton(
                                    action=MessageAction(
                                        label="Message",
                                        text="Hello World!"),
                                    image_url="https://cdn1.iconfinder.com/data/icons/mix-color-3/502/Untitled-1-512.png"
                                ),
                                QuickReplyButton(
                                    action=PostbackAction(
                                        label="Postback",
                                        data="action=buy&itemid=123",
                                        display_text="Buy"
                                    )
                                ),
                                QuickReplyButton(
                                    action=DatetimePickerAction(
                                        label="Datetime Picker",
                                        data="storeId=12345",
                                        mode="datetime",
                                        initial="2018-08-10t00:00",
                                        max="2018-12-31t23:59",
                                        min="2018-08-01t00:00"
                                    ),
                                    image_url="https://icla.org/wp-content/uploads/2018/02/blue-calendar-icon.png"
                                )])
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token, flex_message)

    if text == "A":
            flex = BubbleContainer(
            size = 'kilo', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#ffffff')),
            body = BoxComponent(
                layout='vertical',
                contents=[ButtonComponent(style='primary', # primary,secondary,link
                                          color='#016c9a',
                                          height='sm', # sm,*md
                                          action=MessageAction(
                                              label='check in-out',
                                              text='คุณได้กดปุ่มแล้ว',
                                              type='location'))]))        
            flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
            line_bot_api.reply_message(event.reply_token,flex_message)

if __name__ == "__main__":          
    app.run()

