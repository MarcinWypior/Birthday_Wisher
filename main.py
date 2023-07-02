import pandas
from datetime import datetime
import random
import smtplib

my_email = "marcin1java@gmail.com"
password = "efvrkyjskdqfkcnq"

today = datetime.now()
today_tuple = (today.day ,today.month )
#print(today_tuple)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.day,data_row.month): data_row  for (index,data_row) in data.iterrows()}


#print(birthday_dict)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
        print(contents)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.ehlo()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="marcin1java@op.pl",
                            msg=f"Subject:Happy Birthsday \n\n {contents}")
        connection.close()