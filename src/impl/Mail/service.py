from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL
from fastapi import HTTPException
from sqlalchemy.orm import Session
from Mail import model
from generated_src.lleida_hack_api_client.models.user_get_all import UserGetAll
from schema import MailSchema
from src.impl.Mail.model import Mail as MailModel
from src.impl.Template.model import Template as TemplateModel
from src.utils.Base.BaseService import BaseService


##La idea de aquesta funcio es guardar el correu a la base de dades. Com que no tindrá router, en realitat el archiu no hauria de ser service, no?? :(
##TODO: REVISAR
class MailService(BaseService):

    def get_all(self):
        mail = self.db.query(MailModel).all()
        return mail

    def get_by_id(self, id):
        mail = self.db.query(MailModel).filter(MailModel.id == id).first()
        if mail is None:
            raise Exception()
        return mail

    # def send_email(mail_id: int):
    # @BaseService.needs_service(TemplateService)
    def send(self, mail: MailModel):
        user = None
        msg = MIMEMultipart('related')
        msg['Subject'] = mail.subject
        msg['From'] = Configuration.get('MAIL', 'MAIL_FROM')
        msg['To'] = mail.receiver_mail

        try:
            with SMTP_SSL(Configuration.get('MAIL', 'MAIL_SERVER'),
                          Configuration.get('MAIL', 'MAIL_PORT')) as server:
                server.login(Configuration.get('MAIL', 'MAIL_USERNAME'),
                             Configuration.get('MAIL', 'MAIL_PASSWORD'))
                #send multipart mail adding images withn add_image_attachment and the html
                html = MIMEText(mail.template.to_html(user), 'html')
                msg.attach(html)
                server.sendmail(Configuration.get('MAIL', 'MAIL_FROM'),
                                [user.email], msg.as_string())

                ##TODO: s'hauria de modificar el send a true de la taula de mail.

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
