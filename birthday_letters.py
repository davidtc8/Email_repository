##################### Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
now = dt.datetime.now()
month = now.month
day_of_week = int(now.strftime("%d"))
birthday_tuple = (month, day_of_week)
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
birthdays_df = pd.read_csv("birthdays.csv")
new_dict = {(row.month, row.day):row for (index,row) in birthdays_df.iterrows()}

#birthday_date = {month: day for (month,day) in birthdays}
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if birthday_tuple in new_dict:
    birthday_person = new_dict[birthday_tuple]
    print(birthday_person["name"])

    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    random_letter = f"C:path/{random.choice(letters)}"

    with open(file=random_letter) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person["name"])
        content = content.replace("Angela", "David")
        print(content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = "pythonbot89@gmail.com"
        # Don't let anyone see your password!
        password = "your_password"
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday {birthday_person['name']}!\n\n{content}")

else:
    print("nope")

