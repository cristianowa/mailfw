import zlib
from getpass import getpass


class Login:
    def __init__(self, filename="login"):
        self.filename = filename
        self.user = None
        self.password = None
        try:
            self.getLoginPassword()
        except:
            self.genererateLoginPassword()
            self.getLoginPassword()
    def getLoginPassword(self):
        x = zlib.decompress(open(self.filename).read()).split("\n")
        self.user = x[0]
        self.password = x[1]
    def genererateLoginPassword(self):
        login = raw_input("login\n")
        pwd = getpass("password")
        f = open(self.filename ,"w")
        x = zlib.compress("\n".join([login,pwd]))
        f.write(x)
        f.close()