__author__ = 'huajw'
#coding=utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9900))
# 接收欢迎消息:
print s.recv(1024)
for data in ["jake","jack","jar","java" ]:
    # 发送数据:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()