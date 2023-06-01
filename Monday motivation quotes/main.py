import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "test@gmail.com"
password = "password"

if day_of_week == 1:
    with open("quotes.txt") as data:
        quotes = data.readlines()
        quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@yahoo.com",
            msg=f"Subject:Quotes\n\n{quote}"
        )


