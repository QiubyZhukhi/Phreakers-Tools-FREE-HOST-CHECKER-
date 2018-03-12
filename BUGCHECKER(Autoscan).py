#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print "This is console module"
import socket
from threading import Thread
import os
import sys
import time
dir_proxy_port = "ppp.txt"
dir_site = "site.txt"
timeout = 5
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
os.system("clear")
def slowprint(s):
    print R+"PHREAKERS TOOLS "+W
    print G+" FREE HOST CHECKER WITH PROXY "+W
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(9./90)
slowprint("""
	Author: """+R+
		"""QIUBY """+W+
			"""ZHUKHI"""+O+
				"""\n\t-= [PBM] =- TEAM"""+W+"\r\n")
def site():
    list_site = []
    file = "/storage/emulated/0/{}".format(dir_site)
    site = open(file).readlines()    
    for sites in site:
        sites = sites.split("\n")
        list_site.append(sites[0])
    return list_site
def list_proxy():
    listp = []
    file = "/storage/emulated/0/{}".format(dir_proxy_port)
    buka = open(file).readlines()
    for i in buka:
        n = i.replace("\n", "")
        i = n.split(":")
        listp.append((i[0],int(i[1]))) 
    return listp
def proxy_port(proxy,site):    
    for i in site:
        qz = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        qz.settimeout(timeout)
        try:
            data = "GET http://%s HTTP/1.1\r\nConnection: Keep-Alive\r\nAccept-Encoding: identity; q=1.0, *;q=0 \r\n\r\n" % (i)    
            print i
            print proxy 
            qz.connect(proxy)    
            qz.sendall(data)
            recv = qz.recv(1080).split("\r\n\r\n")[0]
            print recv,"\r\n"
            qz.close()
        except socket.timeout, e:
            print e,"\n"
        except socket.error, e:
            print e,"\n"
listpp = list_proxy()
site = site()
threading = []
if __name__ == "__main__":
    for i in listpp:
        threading.append(Thread(target=proxy_port(i,site)))
    for threadings in threading:
        threadings.start()