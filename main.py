import smtplib
import datetime as dt

my_email = "pythonbot89@gmail.com"
# Don't let anyone see your password!
password = "----"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # tls stands for transport layer security and is a way of securing our connection to our email server
    connection.starttls()
    connection.login(user = my_email, password= password)
    connection.sendmail(from_addr = my_email,
                        to_addrs= "pythonbot89@yahoo.com",
                        msg = "Subject: Hellou\n\nThis is the body of my email")

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year = 1995, month = 12, day = 15)