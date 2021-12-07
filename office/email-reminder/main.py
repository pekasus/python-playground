import smtplib
import datetime as dt
import random

def send_email(message):
    my_gmail = "NyetWork001@gmail.com"
    my_yahoo = "NyetWork001@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    # connection = smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        with open("emailpass.txt", "r") as f:
            password = f.read()

        connection.login(my_gmail, password)
        connection.sendmail(from_addr=my_gmail, to_addrs=my_yahoo,
                            msg=f"Subject:Inspirational Quote\n\n{message}")
    # connection.close()


now = dt.datetime.now() # datatime.datetime object
if now.weekday() == 1:
    with open("quotes.txt", "r") as f:
        lines = f.readlines()
    line = random.choice(lines)
    send_email(line)



# date_of_birth = dt.datetime(year= 1990, month= 1, day= 1)
# print(date_of_birth)
# print(date_of_birth.month)
# print(date_of_birth.weekday())


