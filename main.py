import smtplib
import random
import datetime as dt

my_email = "christian1401.mueller@gmail.com"
password = "cgoiaxqotyhyognx"

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
            to_addrs="christianmueller37@gmail.com",
            msg=f"Subject:Quote of the day\n\n{day_quote}")
