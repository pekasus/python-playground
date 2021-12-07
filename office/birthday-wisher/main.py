from datetime import datetime
import pandas as pd
import random
import smtplib

def send_email(to_email, message):
    my_gmail = "NyetWork001@gmail.com"
    my_yahoo = "NyetWork001@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    # connection = smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        with open("emailpass.txt", "r") as f:
            password = f.read()

        connection.login(my_gmail, password)
        connection.sendmail(from_addr=my_gmail, to_addrs=to_email,
                            msg=f"Subject:Happy Birthday!!!\n\n{message}")


now = datetime.now()
today = (now.month, now.day)
print(today)
df = pd.read_csv("birthdays.csv")
bday_dict = {(datarow.month, datarow['day']):datarow for (index, datarow) in df.iterrows()}


if today in bday_dict:
    name = bday_dict[today]['name']
    email = bday_dict[today]['email']
    letter_file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_file, "r") as f:
        letter = f.read()
    letter = letter.replace("[NAME]", name)
    send_email(email, letter)




