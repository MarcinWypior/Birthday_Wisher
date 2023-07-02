import smtplib
import datetime as dt
import random

now = dt.datetime.now()
my_email = "marcin1java@gmail.com"
password = "efvrkyjskdqfkcnq"



if now.weekday() == 6:
    with open("quotes.txt", "r") as quotes:
        list_of_quotes = quotes.readlines()
        quote_of_day = random.choice(list_of_quotes)
        print(quote_of_day)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.ehlo()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="marcin1java@op.pl", msg=f"Subject:Monday Motivation \n\n {quote_of_day}")
        connection.close()

