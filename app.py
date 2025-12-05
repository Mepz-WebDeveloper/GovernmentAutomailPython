import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_nic_mail(to_email,subject,body,from_email="web-mepz@supportgov.in"):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'html'))
    
    try:
        server = smtplib.SMTP_SSL("smtp.mgovcloud.in",465)
        server.login(from_email,"GZcGhZSeTFME")
        server.send_message(msg)
        server.quit()
        print("Mail send successfully")
        return True
    except:
        try:
            server = smtplib.SMTP("smtp.mgovcloud.in", 587)
            server.starttls()
            server.login(from_email,"Mepz@1030")
            server.send_message(msg)
            server.quit()
            print("Email send TLS")
            return True
        except Exception as e:
            print(f"SMTP Error {e}")
            return False
        
schedule.every().day.at("11:25").do(
lambda:send_nic_mail(to_email="mepzuser15@gmail.com",
              subject="Testing Automail using Government Mail ID",
              body="<h2>Goverment Email</h2><p>You have registered successfully</p>"))

while True:
    schedule.run_pending()
    time.sleep(60)