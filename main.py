import smtplib
import random
import datetime as dt
import os

my_email = os.environ["FROM_MAIL"]
password = os.environ["SMTP_PASSWORD"]

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:

    with open("quotes.txt", mode="r") as quotes:
        quote_list = quotes.readlines()
        day_quote = random.choice(quote_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=os.environ["TO_MAIL"],
            msg=f"Subject:Quote of the day\n\n{day_quote}")
