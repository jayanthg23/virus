import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("jayanthg26@gmail.com", "11111111")
msg="HI"
server.sendmail("jayanthg26@gmail.com","dixitshetty930@gmail.com",msg)
print"succes"
server.quit()
