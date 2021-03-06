import socket, threading, os, sys, datetime, requests, urllib, string, platform, itertools
from json import dumps, loads
from random import choice, shuffle
from time import sleep
from .colors import *


def check_internet(site="http://www.image.google.com") -> bool:
    try:
        request = requests.get(site, timeout=8)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False


def public_ip() -> str:
    int_access = check_internet()
    if int_access:
        ip = urllib.request.urlopen("https://api.ipify.org/").read()
        ip = str(ip)
        ip = ip.strip("{}{}".format("'", string.ascii_letters))
        return ip
    else:
        return "No Internet Access!"


def initialize(nickname, NewPrompt=None) -> str:
    try:
        os.makedirs('Zaphkiel Core')
    except FileExistsError:
        pass
    nameList = []
    ipList = []
    try:
        init_file = open('Zaphkiel Core\\configs.json', 'r').read()
    except FileNotFoundError:
        nickname = input(NewPrompt)
        init_file = open('Zaphkiel Core\\configs.json', 'w')
        init_dict = {}
        

    
class ClientNetwork:
    def __init__(self, nickname, ip=None, port=None) -> None:
        self.nickname = nickname
        self.ip = ip
        self.port = port
        self.date = datetime.datetime.now()
        self.addr = (self.ip, self.port)
        self.buff = 2048
        self.format = 'utf-8'
        self.disc = '{:}{DISC><CON>?'

     
    def create(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.addr)


    def Send(self, message) -> None:
        message_length = len(message)
        message_length = str(message_length).encode(self.format)
        message_length += b' ' * (self.buff - len(message_length))
        message = str(message).encode(self.format)
        self.client.send(message_length)
        self.client.send(message)
    
    
    def SendBytes(self, byteSource) -> None:
        byte_source_length = len(byteSource)
        byte_source_length += b' ' * (self.buff - byte_source_length)
        self.client.send(byte_source_length)
        self.client.send(byteSource)

           
class ServerNetwork:
    def __init__(self, port):
        self.ip = ''
        self.port = port
        self.addr = (self.ip, self.port)
        self.buff = 2048
        self.format = 'utf-8'
        self.disc = '{:}{DISC><CON>?'
        self.Addresses = []
        self.Nicknames = []

    def addressLog(ip, name, date):
        Path = f'{name}\\Address'
        while True:
            try:
                os.makedirs(Path)
                break
            except FileExistsError:
                break
        while True:
            try:
                addr_file = open(f'{Path}\\addr-log.json').read()
                addr_dict = loads(addr_file)
                if addr_dict[f"{ip}"]:
                    keys = addr_dict[f"{ip}"].keys()
                    count = len(keys)
                    addr_dict[f"{ip}"][f"{count+1}"] = f"{date}"
                    new_addr_dict = dumps(addr_dict, indent=3)
                    new_addr_file = open(f'{Path}\\addr_log.json', 'w')
                    new_addr_file.write(new_addr_dict)
                    new_addr_file.close()
                    addr_file.close()
                    break
                else:
                    addr_dict[f"{ip}"] = {}
                    addr_dict[f"{ip}"]["1"] = f"{date}"
                    new_addr_dict = dumps(addr_dict, indent=3)
                    new_addr_file = open(f'{Path}\\addr_log.json', 'w')
                    new_addr_file.write(new_addr_dict)
                    new_addr_file.close()
                    addr_file.close()
                    break
            except FileNotFoundError:
                addr_file = open(f'{Path}\\addr-log.json')
                addr_dict = {}
                addr_log = dumps(addr_dict, indent=3)
                addr_file.write(addr_log)
                addr_file.close()
                continue

    def connectionInit(self, connection) -> tuple:
        nickname_length = connection.recv(self.buff).decode(self.format)
        nickname = connection.recv(int(nickname_length)).decode(self.format)
        date_length = connection.recv(self.buff).decode(self.format)
        date = connection.recv(date_length).decode(self.format)
        return (nickname, date)

    def create(self):
        print(f'[Server]: Starting the Server....')
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.addr)

    def Start(self, handler=None, commander=None, broadcaster=None, Channel=None):
        self.server.listen()
        print(f'[Server]: Server was binded on {socket.gethostbyname(socket.gethostname())} successfully!')
        while True:
            print('\n    >> [Server]: Waiting for new connections....')
            conn, addr = self.server.accept()
            print(f'\n  [Server]: {addr} has been connected!')
            Ip, conPort = addr
            nickname, date = self.connectionInit(conn)
            self.addressLog(Ip, nickname, date)
            '''thread = threading.Thread(target=handler, args=(conn, addr))
            thread.start()'''

    def ServerStart(self):
        self.create()
        self.Start()
            

