import smtplib
from email.mime.text import MIMEText                            

def send_alert(indicator):
    from_gmail = 'System <nucleoklient@gmail.com>'
    to_gmail = 'Admin <nucleoklient@gmail.com>'
    username = '' # email without @gmail.com
    password = '' # password from email
    msg= MIMEText((str(indicator)+' : показатель вышел за пределы нормы! \n ').encode('utf-8'), _charset='utf-8')
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login(username, password)
    smtpObj.sendmail(from_gmail, to_gmail, 'Subject: Nucleo system notification! \n{}'.format(msg))
    smtpObj.quit()
