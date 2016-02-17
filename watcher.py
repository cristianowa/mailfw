from reader import Reader
from mail import  Mailer
class Watcher:
    def __init__(self, readserver, readlogin, readport, sendserver, sendfrom, sendto, sendlogin, prefix):
        self.reader = Reader(readlogin, readserver, readport)
        self.sender = Mailer(sendlogin, sendfrom, sendserver)
        self.sendto = sendto
        self.prefix = prefix
    def action(self):
        unreaded =self.reader.get_unread()
        for ur in unreaded:
            self.sender.send(self.sendto, self.prefix + ur.headers.Subject, ur.string)
            print "Sending " + ur.headers.Subject
if __name__ == '__main__':
    w = Watcher("imap.inf.ufrgs.br",".inf", 993,  "smtp.zoho.com", "contato@procuratio.net.br",
                [ "cristianowerneraraujo@gmail.com"],".login", "[FWINF]")
    w.action()