from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import sys

# proto_cmds = FTPHandler.proto_cmds.copy()
# proto_cmds.update(
#     {'ADD1': dict(perm='R',auth=True,arg=True)}
# )

def add(a,b):
    a = float(a)
    b = float(b)
    return a+b
def add1(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    return a+b+c


class NewHandler(FTPHandler):
    def on_file_sent(self,file):
        # f = open(file,'r')
        # line = f.readlines()
        # func = line[0]
        
        # op1 = line[1]
        # op2 = line[2]
        # data = add(op1,op2)
        # f.write(data)
        # f.close()
        output = './lab4/output.txt'
        # print('sentt')
        os.remove(output)
        pass
    def on_file_received(self,file):
        print('revdd')
        f = open(file,'r')
        line = f.readlines()
        print(line[0])
        line1 = eval(line[0])
        print(line1[1])
        if len(line1) == 3:
            line = add(line1[1],line1[2])
        if len(line1) == 4:
            line = add1(line1[1],line1[2],line1[3])
        output = './lab4/output.txt'
        f1 = open(output,'w')
        f1.write(str(line))
        f1.close()
        # print('write')
        os.remove(file)
        pass    
    # def on_file_u
    # proto_cmds = proto_cmds
#     def ADD1(self):
#         return 1
    
# def ADD1(self):
#     return 1+2

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", ".", perm="elradfmw")
authorizer.add_anonymous(".", perm="elradfmw")

handler = NewHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()