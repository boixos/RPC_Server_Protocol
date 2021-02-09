from ftplib import FTP
import rpc


while 1:
    cmd = input()
    params = cmd.split(' ')
    if params[0]  == 'add':
        rpc.uploadFile(params)
        data = rpc.downloadFile()
        print(data)
    else:
        print('Invalid Input')    
 