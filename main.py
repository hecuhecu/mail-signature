import smtplib
import ssl
from email.mime.text import MIMEText

def create_message(to, sub, body, sender):
    msg = MIMEText(body)
    msg["To"] = to
    msg["Subject"] = sub
    msg["From"] = sender

    return msg

def add_signature(body):
    signature = "\n\n" + "---------------------------------" + "\n" + "関西学院大学 理工学部 情報科学科 3年" + "\n" \
                + "河村 宇記（Hiroki Kawamura）" + "\n" + "Tel: 070-5662-5782" + "\n" + "Mail: hecunyuji5@gmail.com" \
                + "\n" + "---------------------------------"
    body += signature

    return body

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

    #署名の追加
    body = add_signature(body)

    #メール作成
    msg = create_message(to, subject, body, gmail_account)

    #メール送信
    send_message(msg, gmail_account, gmail_password)

if __name__ == "__main__":
    main()