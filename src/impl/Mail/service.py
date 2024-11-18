from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

from fastapi import HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy import asc, desc

# from src.Clients.UserClient import UserClient
from src.configuration.Configuration import Configuration
from src.impl.Mail.model import Mail as MailModel
from src.impl.Mail.schema import MailCreate as MailCreateSchema
# from src.utils.Base.BaseClient import BaseClient
from src.utils.Base.BaseService import BaseService
from src.utils.service_utils import set_existing_data


class MailService(BaseService):
    name = 'mail_service'
    user_client = None

    def get_all(self):
        mail = db.session.query(MailModel).all()
        return mail

    def get_by_id(self, id) -> MailModel:
        mail = db.session.query(MailModel).filter(MailModel.id == id).first()
        if mail is None:
            raise Exception()
        return mail

    # @BaseClient.needs_client(UserClient)
    def create(self, payload: MailCreateSchema):
        mail = MailModel(**payload.dict(), sent=False)
        db.session.add(mail)
        # self.user_client.get_by_id(mail.receiver_id)
        # self.user_client.get_by_id(mail.sender_id)
        db.session.commit()
        return mail

    def update(self, id: int, payload: MailCreateSchema):
        mail = self.get_by_id(id)
        update = set_existing_data(mail, payload)
        db.session.commit()
        db.session.refresh(mail)
        return mail, update

    def set_sent(self, mail: MailModel):
        if mail.sent:
            raise Exception("An exception occurred.")
        mail.sent = True
        db.session.commit()
        db.session.refresh(mail)

    def send_by_id(self, id: int):
        mail = self.get_by_id(id)
        if mail.sent:
            Exception('sent?')
        r = self.real_send(mail)
        self.set_sent(mail)
        return r

    def send_next(self):
        mail = db.session.query(MailModel).filter(
            MailModel.sent == False).order_by(desc(
                MailModel.priority)).order_by(asc(
                    MailModel.creation_date)).first()
        if mail is None:
            raise Exception("no more mails avaliable")
        if mail.sent:
            raise Exception("suposadament no possible")
        self.real_send(mail)
        self.set_sent(mail)

    def clear_next_mail(self):
        print("HOLA")
        mail = db.session.query(MailModel).filter(
            MailModel.sent == False).order_by(desc(
                MailModel.priority)).order_by(asc(
                    MailModel.creation_date)).first()
        print(mail)
        if mail is None:
            raise Exception("no more mails avaliable")
        if mail.sent:
            raise Exception("suposadament no possible")
        self.set_sent(mail)

    def clear_mail_queue(self):
        mails = db.session.query(MailModel).filter(
            MailModel.sent == False).order_by(desc(
                MailModel.priority)).order_by(asc(MailModel.creation_date))
        if mails == []:
            raise Exception("no more mails avaliable")
        for mail in mails:
            self.set_sent(mail)

    def real_send(self, mail: MailModel):
        # u = self.user_client.get_by_id(mail.sender_id)
        msg = MIMEMultipart('related')
        msg['Subject'] = mail.subject
        msg['From'] = Configuration.mail.from_mail
        msg['To'] = mail.receiver_mail
        try:
            html = MIMEText(mail.template.to_html(mail.fields.split(',')),
                            'html')
            msg.attach(html)
            if Configuration.mail.send_mails:
                # server.sendmail(Configuration.mail.from_mail, [user.email],
                with SMTP_SSL(Configuration.mail.server,
                              Configuration.mail.port) as server:
                    server.login(Configuration.mail.username,
                                 Configuration.mail.password)
                    server.sendmail(
                        Configuration.mail.from_mail,
                        [mail.receiver_mail.replace(' ', '').split(',')],
                        msg.as_string())
            else:
                print(
                    'Mail sending is disabled i you really want to send mails enable it in the config'
                )
        except Exception as e:
            raise e
            raise HTTPException(status_code=500, detail=str(e))

    # def real_send_api():
