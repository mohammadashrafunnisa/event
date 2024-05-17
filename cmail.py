import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('mohammadashrafunnisa9@gmail.com','xooy qbqz vfhr gtok')
    msg=EmailMessage()
    msg['FROM']='mohammadashrafunnisa9@gmail.com'
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

