import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


def send_email(subject, body, to_email, from_email, from_password, smtp_server, smtp_port):
    # 创建MIMEMultipart对象
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # 附加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # 连接到SMTP服务器并发送邮件
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {to_email} successfully.")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")


def create_daily_report():
    # 这里生成你的报告内容
    report_content = "这是每日报告的内容(qyf)。"
    return report_content


if __name__ == "__main__":
    # 电子邮件配置信息
    TO_EMAIL = "752971750@qq.com"
    FROM_EMAIL = "yunfei2016@foxmail.com"
    FROM_PASSWORD = "dswegjhrhzpxdiid"
    SMTP_SERVER = "smtp.qq.com"
    SMTP_PORT = 587

    # 创建报告并发送邮件
    subject = f"每日报告 - {datetime.now().strftime('%Y-%m-%d')}"
    body = create_daily_report()
    send_email(subject, body, TO_EMAIL, FROM_EMAIL, FROM_PASSWORD, SMTP_SERVER, SMTP_PORT)
