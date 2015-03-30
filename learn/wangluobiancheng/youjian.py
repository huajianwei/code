__author__ = 'huajw'
#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(),addr.encode('utf-8') if isinstance(addr, unicode) else addr))

#msg = MIMEText('hello,\t can you see the text? ', 'plain', 'utf-8')
msg = MIMEText('确实是的,我就是这么屌,你怎么滴, 这个一个自动发送的邮件,请不要回复,你回复我也不看,,,send by 滑建威 这句话是测试用的', 'plain', 'utf-8')
msg['From'] =  _format_addr(u'滑建威<%s>'% formataddr)
msg['To'] = _format_addr(u'最真诚的你<%s>'% formataddr)
msg['Subject'] = Header(u'这是一封电脑自动发出的邮件', 'utf-8').encode()


#发送邮件
# 输入Email地址和口令:
from_addr = "lxyxxb2010@yeah.net"
password = '123321'
# 输入SMTP服务器地址:
smtp_server = 'smtp.yeah.net'
# 输入收件人地址:
to_addr = '2423076451@qq.com'


server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()