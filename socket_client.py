import socket
import time
s=socket.socket()

host= socket.gethostname()

port=233

s.connect((host,port))
def get_data(bytes_data):
    return str(bytes_data,encoding='utf-8')

def send_data(str_data):
    return bytes(str_data,encoding='utf-8')


while True:
    recv_data =s.recv(1024)
    time.sleep(1)
    print(get_data(recv_data))

    s.send(send_data('这是客户端：'+str(time.time())))

