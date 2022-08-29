import socket
import keyboard as k
import time as t

with open('settings_s.txt', 'r') as s:
    set = s.readlines()
hot_list = []
for i in range(18):
    hot = set[i].strip(str(i+1)+' -').strip('\n')
    hot_list.append(hot)
print(hot_list)
host = set[20].strip('ipv4 = ').strip()
port = int(set[19].strip('port = ').strip())
print(host,port)


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()
user,adr = server.accept()
print('connected')
while True:
    data = None
    data = user.recv(1024)
    data_d = data.decode('utf-8')
    print(data_d)
    if int(data_d) in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
        if len(hot_list[int(data_d)-1]) != 0:
            k.press(hot_list[int(data_d)-1])
            t.sleep(0.1)
            k.release(hot_list[int(data_d)-1])
            print(f'{hot_list[int(data_d)-1]} pressed')
    if data.decode('utf-8') == 'Man u need close':
        break
