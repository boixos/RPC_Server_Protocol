from ftplib import FTP
import time,os,sys


def uploadFile(params):
    ftp = FTP('')
    ftp.connect('localhost',1026)
    ftp.login()
    ftp.cwd('lab4') #replace with your directory
    # ftp.retrlines('LIST')

    
    filename = 'testfile.txt' 
    f = open(filename, 'w')
    data = str(params)
    f.write(data)
    f.close()
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    os.remove('testfile.txt')
    #  downloadFile()

    ftp.quit()

def downloadFile():
    ftp = FTP('')
    ftp.connect('localhost',1026)
    ftp.login()
    ftp.cwd('') #replace with your directory
    # ftp.retrlines('LIST')

    filename = 'output1.txt' #replace with your file in the directory ('directory_name')
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + '/lab4/output.txt', localfile.write, 1024)
    ftp.quit()
    localfile.close()
    f = open('output1.txt','r')
    line = f.readline()
    os.remove('output1.txt')
    return line

