import time
import smtplib

####################################
####################################

###Email setup stuff:
sendToAddress = 'jodalyst@mit.edu'
fromAddress = 'mostecelectronics2015@gmail.com'
username = 'mostecelectronics2015'
password = 'mostecmostec2015'


message = "HEY THERE FRIEND!!"

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromAddress, sendToAddress,message)
server.quit()

