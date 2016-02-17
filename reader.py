import imaplib
from login import Login

class Reader():
    def __init__(self, login, server, port):
        self.login = Login(login)
        self.server = server
        self.port = port
    def get(self):
        M = imaplib.IMAP4_SSL(self.server, self.port)
        M.login(self.login.user, self.login.password)
        M.select()
        typ, data = M.search(None, 'ALL')
        for num in data[0].split():
            typ, data = M.fetch(num, '(RFC822)')
            print 'Message %s\n%s\n' % (num, data[0][1])
        M.close()
        M.logout()

if __name__ == '__main__':
    r = Reader(".inf","imap.inf.ufrgs.br", 993)
    r.get()
