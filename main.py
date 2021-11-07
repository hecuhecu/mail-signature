import smtplib
import ssl
from email.mime.text import MIMEText

def create_message(to, sub, body, sender):
    msg = MIMEText(body)
    msg["To"] = to
    msg["Subject"] = sub
    msg["From"] = sender

    return msg

def send_message(msg, id, pw):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
    server.login(id, pw)
    server.send_message(msg)
    server.close()
    print("送信完了")

def main():
    #gmailログイン用のデータ
    gmail_account = "hecunyuji5@gmail.com"
    gmail_password = "kawamura0628"

    #宛先,件名,本文(exitで終了)を入力
    to = input("to: ")
    subject = input("subject: ")
    print("message: ")
    body = "\n".join(iter(input, "exit"))

    #メール作成
    msg = create_message(to, subject, body, gmail_account)

    #メール送信
    send_message(msg, gmail_account, gmail_password)

if __name__ == "__main__":
    main()