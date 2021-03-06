def log(msg):
	print(msg)

class MailConfig:
	POP_SERVER_NAME = "mail.fudan.edu.cn"
	SMTP_SERVER_NAME = "mail.fudan.edu.cn"

import poplib, smtplib
from email import message_from_string, mime
from email.utils import formatdate
from getpass import *

class PopClient:
	def __init__(self, user, pwd, host = MailConfig.POP_SERVER_NAME):
		self.server = poplib.POP3(host)
		self.server.user(user)
		self.server.pass_(pwd)
	
	def fetch(self, index):
		"""
		index starts from 1
		"""
		raw = self.server.retr(index)[1]
		msg = message_from_string('\n'.join(raw))
		return msg

class SmtpClient:
	def __init__(self, user, pwd, host = MailConfig.SMTP_SERVER_NAME):
		self.server = smtplib.SMTP(host)
		self.server.login(user, pwd)
			
	def send(self, fro, to, subject, content):
		"""
		send an email from 'fro' to 'to'
		'to' should be a list
		"""
		msg = mime.Multipart.MIMEMultipart()
		msg['From'] = fro
		msg['To'] = ', '.join(to)
		msg['Subject'] = subject 
		msg['Date'] = formatdate(localtime=True) 
		msg.attach(mime.Text.MIMEText(content))
		
		self.server.sendmail(fro, to, msg.as_string())

if __name__ == '__main__':
	pass
	#smtp.send("10300240067@fudan.edu.cn", ["x_c0@163.com"], "tasdasdest", "hehehehehehe")
