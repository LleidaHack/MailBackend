from fastapi import HTTPException
from sqlalchemy.orm import Session
from Mail import model
from schema import MailSchema

##La idea de aquesta funcio es guardar el correu a la base de dades. Com que no tindrá router, en realitat el archiu no hauria de ser service, no?? :(
##TODO: REVISAR
def send_email(mail_id: int):
    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = Configuration.get('MAIL', 'MAIL_FROM')
    msg['To'] = email

    try:
        with SMTP_SSL(Configuration.get('MAIL', 'MAIL_SERVER'),
                      Configuration.get('MAIL', 'MAIL_PORT')) as server:
            server.login(Configuration.get('MAIL', 'MAIL_USERNAME'),
                         Configuration.get('MAIL', 'MAIL_PASSWORD'))
            #send multipart mail adding images withn add_image_attachment and the html
            html = MIMEText(template, 'html')
            msg.attach(html)
            server.sendmail(Configuration.get('MAIL', 'MAIL_FROM'), [email],
                            msg.as_string())
            
            ##TODO: s'hauria de modificar el send a true de la taula de mail.
      
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

