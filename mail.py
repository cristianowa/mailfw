import smtplib
import login

def send(frm, to, subject, msg):
    message = """\
From: %s
To: %s
Subject: %s

%s
    """ % (frm, ", ".join(to), subject, msg)
    s = smtplib.SMTP_SSL("smtp.zoho.com")
    s.login(login.user, login.password)
    s.sendmail(frm, to, message)

if __name__ == "__main__":
    send("contato@procuratio.net.br", [ "cristianowerneraraujo@gmail.com", "contato@procuratio.net.br"],"A test", "A simple test")

