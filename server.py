'''
Author: Fczhao
Date: 2023-05-09 16:21:45
'''
import socket
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#定义ip地址与端口号，ip地址就是服务端的ip地址，端口随便定义，但要与客户端脚本一致
ip_port = ('127.0.0.1',8000)
#绑定一个端口
sk.bind(ip_port)
#监听一个端口,这里的数字3是一个常量，表示阻塞3个连接，也就是最大等待数为3
sk.listen(3)
#接受客户端的数据，并返回两个参数，a为连接信息，b为客户端的ip地址与端口号
a,b=sk.accept()
print(a)
while True:
    data=a.recv(1024)#客户端发送的数据存储在recv里，1024指最大接受数据的量
    print(data.decode('utf-8'))
    message=input("you can say:")
    a.send(message.encode('utf-8'))
    if message==('bye'):
        break
