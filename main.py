# import smtplib
# from getpass import getpass
#
# my_email = "marcin1java@gmail.com"
# password = "efvrkyjskdqfkcnq"
#
# try:
#     connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     connection.ehlo()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="marcin1java@op.pl", msg="Hello")
#     connection.close()
#     print("Email sent successfully!")
# except Exception as e:
#     print("An error occurred while sending the email:", e)
#
import smtplib

my_email = "marcin1java@gmail.com"
password = "efvrkyjskdqfkcnq"

connection = smtplib.SMTP_SSL("smtp.gmail.com")
connection.ehlo()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="marcin1java@op.pl", msg="Hello")
connection.close()