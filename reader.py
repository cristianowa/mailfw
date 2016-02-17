import imaplib
import email
from login import Login
from exdict import Exdict
class Email:
    def __init__(self, string):
        self.string = string
        self.email = email.message_from_string(string)
        self.headers = Exdict(self.email._headers)


class Reader():
    def __init__(self, login, server, port):
        self.login = Login(login)
        self.server = server
        self.port = port
    def get(self, filter = 'ALL'):
        M = imaplib.IMAP4_SSL(self.server, self.port)
        M.login(self.login.user, self.login.password)
        M.select()
        emails = []
        typ, data = M.search(None, filter)
        for num in data[0].split():
            typ, data = M.fetch(num, '(RFC822)')
            msg = Email(data[0][1])
            emails.append(msg)
        M.close()
        M.logout()
        return emails
    def get_unread(self):
        return self.get("(UNSEEN)")
    def get_subject_contains(self, filter):
        emails = self.get()
        ret = []
        for m in emails:
            if m.headers.Subject.__contains__(filter):
                ret.append(m)
        return ret
if __name__ == '__main__':
    r = Reader(".inf","imap.inf.ufrgs.br", 993)
    s = r.get_subject_contains("Prosoft")
    for i in s:
        print i.headers.Subject
    #print r.get_unread()
