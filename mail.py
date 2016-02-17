import smtplib

from login import Login


class Mailer:
    def __init__(self, login, frm, server):
        self.login = Login(login)
        self.frm = frm
        self.server = server
    def send(self, to, subject, msg):
        message = """\
From: %s
To: %s
Subject: %s

%s
    """ % (self.frm, ", ".join(to), subject, msg)
        s = smtplib.SMTP_SSL(self.server)
        s.login(self.login.user, self.login.password)
        s.sendmail(self.frm, to, message)

if __name__ == "__main__":
    m = Mailer(".login", "contato@procuratio.net.br", "smtp.zoho.com")
    m.send([ "cristianowerneraraujo@gmail.com"],"A new test", "A simple test")


