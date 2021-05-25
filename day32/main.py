##################### Hard Starting Project ######################
import smtplib
from datetime import datetime
import pandas
import random

MY_EMAIL = "nightstarke4@gmail.com"
MY_PASSWORD = "THIENHA1"

to_day = datetime.now()
today_tuple = (to_day.month, to_day.day)
print(today_tuple)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]["name"]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        letter = contents.replace("[NAME]", birthday_person)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="nightstarke7@gmail.com",
            msg=letter
        )

