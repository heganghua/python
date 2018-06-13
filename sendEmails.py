#-*- coding:utf-8 _*-  
""" 
@author:华仔 
@file: smtplib.py 
@time: 2018/05/{DAY} 
"""  


import smtplib  
from email.header import Header
from email.mime.text import MIMEText
  
# 第三方 SMTP 服务  
mail_host = "smtp.163.com"      # SMTP服务器  
mail_user = 'heganghua1113@163.com'                  # 用户名  
mail_pass = "heganghua1113"               # 授权密码，非登录密码  
  
sender =' heganghua1113@163.com'    # 发件人邮箱(最好写全, 不然会失败) 
receivers = ['1315579747@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱  
  
content = '我用Python'  
title = '人生苦短'  # 邮件主题  
  
def sendEmail():  
  
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码  
    message['From'] = "{}".format(sender)  #发送方账号
    message['To'] = ",".join(receivers)  	#发送给谁
    message['Subject'] = title  			#标题
  
    try:  
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465  
        smtpObj.login(mail_user, mail_pass)  # 登录验证  
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送 
        print("mail has been send successfully.")  
    except smtplib.SMTPException as e:  
        print(e)  
  
def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):

    email_client = smtplib.SMTP(SMTP_host) 			 #启用SMTP发信  参数为SMTP服务器
    email_client.login(from_account, from_passwd)    #登陆，密码和授权密码
    # create msg  
    msg = MIMEText(content, 'plain', 'utf-8')		 #内容， 格式， 编码
    msg['Subject'] = Header(subject, 'utf-8')  		 # 标题
    msg['From'] = from_account  					 # 发送方
    msg['To'] = to_account  						 # 接收方
    email_client.sendmail(from_account, to_account, msg.as_string())	#发送  
  
    email_client.quit()		#退出
  
if __name__ == '__main__':  
    #sendEmail()  
    receiver = "1315579747@qq.com"
    send_email2(mail_host, mail_user, mail_pass, receiver, title, content)  