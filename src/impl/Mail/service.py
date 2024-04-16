from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from fastapi import HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy import asc, desc
from src.configuration.Configuration import Configuration
from src.impl.Mail.model import Mail as MailModel
from src.utils.Base.BaseService import BaseService
from src.impl.Mail.schema import MailCreate as MailCreateSchema
from src.utils.service_utils import set_existing_data


class MailService(BaseService):
    name = 'mail_service'
    
    def get_all(self):
        mail = db.session.query(MailModel).all()
        return mail

    def get_by_id(self, id) -> MailModel:
        mail = db.session.query(MailModel).filter(MailModel.id == id).first()
        if mail is None:
            raise Exception()
        return mail

    def create(self, payload: MailCreateSchema):
        mail = MailModel(**payload.dict(), sent=False)
        db.session.add(mail)
        db.session.commit()
        return mail

    def update(self, id: int, payload: MailCreateSchema):
        mail = self.get_by_id(id)
        update = set_existing_data(mail, payload)
        db.session.commit()
        db.session.refresh(mail)
        return mail, update

    def set_sent(mail: MailModel):
        if mail.sent:
            raise Exception("An exception occurred.")
        mail.sent = True
        db.session.commit()
        db.session.refresh(mail)

    def send_by_id(self, id: int):
        mail = self.get_by_id(id)
        if mail.sent:
            Exception()
        self.real_send(mail)
        self.set_sent(mail)

    def send_next(self):
        mail = db.session.session.query(MailModel).filter(
            MailModel.sent == False).order_by(desc(
                MailModel.priority)).order_by(asc(
                    MailModel.creation_date)).first()
        if mail is None:
            raise Exception()
        if mail.sent:
            Exception()
        self.real_send(mail)
        self.set_sent(mail)

    def real_send(self, mail: MailModel):
        user = None
        msg = MIMEMultipart('related')
        msg['Subject'] = mail.subject
        msg['From'] = Configuration.mail.from_mail
        msg['To'] = mail.receiver_mail
        try:
            with SMTP_SSL(Configuration.mail.server,
                          Configuration.mail.port) as server:
                server.login(Configuration.mail.username,
                             Configuration.mail.password)
                html = MIMEText(mail.template.to_html(user), 'html')
                msg.attach(html)
                if Configuration.mail.send_mails:
                    server.sendmail(Configuration.mail.from_mail, [user.email],
                                    msg.as_string())
                else:
                    print(
                        'Mail sending is disabled i you really want to send mails enable it in the config'
                    )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
