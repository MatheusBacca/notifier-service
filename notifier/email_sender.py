import smtplib
from email.mime.text import MIMEText

from notifier.notifier_base import NotifierBase


class Email(NotifierBase):
    def __init__(self):
        self.sender_email = self.config["email"]["sender"]
        self.smtp_server = self.config["email"]["smtp_server"]
        self.smtp_port = self.config["email"]["smtp_port"]
        self.smtp_password = self.config["email"]["smtp_password"]

    def send(self, recipient, content):
        msg = MIMEText(content)
        msg["Subject"] = "Notificação"
        msg["From"] = self.sender_email
        msg["To"] = recipient

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.sender_email, self.smtp_password)
            server.sendmail(self.sender_email, recipient, msg.as_string())
