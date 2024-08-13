#region library
import smtplib
from email.message import EmailMessage
#endregion library

#region Global
Email_Host = "smtp.gmail.com"
Email_Host_User = "report.riazmand@gmail.com"  #App email
Email_Port_SSL = 465
Email_Host_pass = "rrbu hoci gsgz tvph "
Email_getter = "MrArminDM@gmail.com"  #My email
#Email_getter = "khzitcenter@gmail.com"  #The provincial referee's email

#endregion Global
#region Main
def crash_mail(erorr):
    subject = "Riazmand was crashed!"
    massage = f"Riazmand was crashed in the test\n Erorr:"
    main_massage = erorr

    return msg(subject, massage, main_massage)

def close_mail():
    subject = "Riazmand was closed!"
    massage = f"Riazmand closed\n Erorr:"
    main_massage = "Program closed by user."

    return msg(subject, massage, main_massage)

def msg(subject, massage, main_massage):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'Riazmand'
    msg['To'] = Email_getter
    msg.set_content(massage)
    msg.add_alternative(f"""
    <body>
    	<p><b> {main_massage} </b></p>
    </body>
    """, subtype='html')

    try:
        with smtplib.SMTP_SSL(Email_Host, Email_Port_SSL) as server:
            server.login(Email_Host_User, Email_Host_pass)
            server.send_message(msg)
        return True
    except:
        return False
#endregion Main
