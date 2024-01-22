# นำเข้าไลบรารีที่จำเป็น
from flask import Flask, request, abort
from threading import Event
import pandas as pd
import webbrowser
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from openpyxl import load_workbook
from linebot.models import (MessageEvent,TextMessage,FlexSendMessage,BubbleContainer,BoxComponent,TextComponent,
BubbleStyle,BlockStyle,CarouselContainer,ImageComponent,MessageAction,ButtonComponent,URIAction,LocationAction,)
import os
import requests, urllib.parse
from email.message import EmailMessage
import smtplib
import json
import psycopg2
from psycopg2.extras import RealDictCursor
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from linebot.models import FlexSendMessage


app = Flask(__name__)
channel_secret = "78e93310e943248a7a53639cb1b668b7"
channel_access_token = "0EB6kJ8Npso89qsPBaTFxrpYsvmE6ei7lvMr7KzdMHRxW4AQUUo9ucAF7oTONjPDppSNCViu5+r7frw6EsT+XCpbx9uet8iAElaGk3kr1BA8bXaUGPaVt+WbrKiDfk3EwDUhKR8HnvO6jHShB2DAygdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',  # ใช้ localhost
                            port='4444',  # ใช้พอร์ตที่ตั้งไว้
                            database='user_info',
                            user='username',  # แทนที่ username ของคุณ
                            password='1234')  # แทนที่ password ของคุณ
    return conn

def send_email(to_email, subject, body, sender_email, sender_password):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def update_user_status(user_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE user_info SET status_mail = 'Y' WHERE id = %s", (user_id,))
        conn.commit()
    except Exception as e:
        print(f"Error updating user status: {e}")
    finally:
        cur.close()
        conn.close()


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

        # ดึง userId จาก event.source
    user_id = event.source.user_id
    text = event.message.text
    print(user_id)
    print(text)

    if text == "ลบ":
            user = str(user_id)
            conn = get_db_connection()
            cur = conn.cursor()
            print(user_id)

            outtext = "ลบเรียบร้อย"
            line_bot_api.reply_message(
                line_bot_api.reply_message(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=outtext)]
                )
            )

            try:
                # สร้างคำสั่ง SQL สำหรับลบข้อมูล
                delete_script = 'DELETE FROM user_info WHERE id = %s'
                delete_value = (user_id,)
                
                # ทำการ execute คำสั่ง SQL
                cur.execute(delete_script, delete_value)
                
                # Commit ทำการยืนยันการเปลี่ยนแปลง
                conn.commit()
                
                print("Data deleted successfully!")

            except Exception as e:
                # Rollback ในกรณีเกิดข้อผิดพลาด
                conn.rollback()
                print(f"An error occurred: {e}")

            finally:
                # ปิด cursor และ connection
                cur.close()
                conn.close()


    if text == "จด":
            user = str(user_id)
            conn = get_db_connection()
            cur = conn.cursor()
            name = "วงศธร สิงห์แสงภัณฑ์"
            email = "wongsaton0922495138@tracthai.com"
            phone = "2345235333"
            print(user_id)
            try:
                insert_script = 'INSERT INTO user_info(id,username,email,phone_number) VALUES (%s,%s,%s,%s)'
                insert_value = (user_id,name,email,phone)
                cur.execute(insert_script, insert_value)
                
                # Commit the transaction to apply the changes
                conn.commit()
                
                print("Data inserted successfully!")

            except Exception as e:
                # Rollback the transaction in case of an error
                conn.rollback()
                print(f"An error occurred: {e}")

            finally:
                cur.close()
                conn.close()


    if text == "แจ้ง" :
            user = str(user_id)
            conn = get_db_connection()
            cur = conn.cursor()
            print(user_id)
            try:
                cur.execute("SELECT username, email FROM user_info WHERE id = %s", (user,))
                user_data = cur.fetchone()
                print(user_data)
                if user_data:
                    username, email = user_data
                    print(f"Email: {email}, Username: {username}")
                
                    subject = "ทดสอบการส่งอีเมล"
                    body = f"""
                    <html>
                    <head>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                background-color: #f4f4f4;
                                color: #333;
                                text-align: center;
                                padding: 50px;
                            }}
                            h1 {{
                                color: #4CAF50;
                            }}
                            p {{
                                font-size: 16px;
                            }}
                            .container {{
                                background-color: #fff;
                                margin: auto;
                                padding: 20px;
                                border-radius: 8px;
                                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
                                max-width: 600px;
                            }}
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <h1>สวัสดีครับคุณ : {username}</h1>
                            <p>นี่คือข้อความจากอีเมลที่ถูกออกแบบอย่างมืออาชีพ.</p>
                            <p>ขอบคุณที่ใช้บริการของเรา!</p>
                        </div>
                    </body>
                    </html>
                    """
                    
                    if send_email(email, subject, body, "report.trac@gmail.com", "mcoqvwpabjtdoxvw"):
                        update_user_status(user_id)
                        # ส่งกลับไปบอกว่า ส่งเมลเรียบร้อย
                        line_bot_api.reply_message(
                            line_bot_api.reply_message(
                                reply_token=event.reply_token,
                                messages=[TextMessage(text="ส่งเมลเรียบร้อย")]
                            )
                        )
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                cur.close()
                conn.close()

if __name__ == "__main__":
    app.run()
   
