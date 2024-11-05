import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
current_dir = os.getcwd()

print("""
------------------------------------------------------
             || WELCOME TO CODE EMAIL||
             ||     DEVELOPED BY     ||
             ||    YASH AUDICHYA     ||
             ||     version 1.0      ||
------------------------------------------------------

""")
code=input("enter your code file name : ")
emaill=input("enter your email : ")

def sendemail(email,code):
    smtp_server="smtp.gmail.com"
    port = 587  # For TLS
    sender_email = "YOUR EMAIL"
    app_password = "PASSWORD"  # Use your app password here
    receiver_email = email
    subject = "Your code"
    body = f"{code} \n ||=====developed by yash=====||"
    return smtp_server,port,sender_email,app_password,receiver_email,subject,body

program_path = os.path.join(current_dir, code)
with open(program_path,'r') as file:
    lines=file.read()

smtp_server,port,sender_email,app_password,receiver_email,subject,body=sendemail(emaill,lines)

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    with smtplib.SMTP(smtp_server, port) as server:
        print("wait a second...")   
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, app_password)  # Login using your email and app password
        server.sendmail(sender_email, receiver_email, msg.as_string())  # Send email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
