import socket
import time 
soc= socket.socket()

host= socket.gethostname()
port=233
soc.bind((host,port))

soc.listen(5)   # 等待客户端连接数

def get_data(bytes_data):
    return str(bytes_data,encoding='utf-8')

def send_data(str_data):
    return bytes(str_data,encoding='utf-8')

c,addr=soc.accept() # 建立client连接
while True:
    time.sleep(1)
    print('client地址：',addr)
    msg="来了？老弟："+ str(time.time())
    c.send(send_data(msg))
    print(msg)

    xx = c.recv(1024)

    print(111,get_data(xx))
   
    # c.send(')
    # c.send('来了？老弟：'+str(addr,encoding='utf-8'))
    