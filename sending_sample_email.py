
import smtplib

sender = "cjain9975@gmail.com"
password = "x"
receiver = "cjain9975@gmail.com"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, "Subject: Test\n\nHello Chirag, this is a test.")
