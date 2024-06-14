##################### Extra Hard Starting Project ######################
import os.path
import pandas as pd
import datetime as dt
import smtplib as mail
import random as rd

SENDER = os.getenv("MY_GMAIL")
PASSWD = os.getenv("MY_GMAIL_APP_PASSWD")
df = pd.read_csv("birthdays.csv")
match_birthdate = {}


def check_birthday():
    global match_birthdate
    current = dt.datetime.now()
    match_birthdate = df[(df['month'] == current.month) & (df['day'] == current.day)]
    if not match_birthdate.empty:
        return True
    else:
        return False


def get_letter(name):
    placeholder = "[NAME]"
    folder_path = "./letter_templates"
    selected_letter = rd.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
    selected_file_path = os.path.join(folder_path, selected_letter)

    with open(selected_file_path, "r") as letter_file:
        letter_content = letter_file.read()
        new_letter = letter_content.replace(placeholder, name)

    return new_letter


def send_email():
    if check_birthday():
        for _, row in match_birthdate.iterrows():
            name = row["name"]
            receiver = row["email"]
            letter = get_letter(name)

            with mail.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=SENDER, password=PASSWD)
                connection.sendmail(
                    from_addr=SENDER,
                    to_addrs=receiver,
                    msg="Subject:Happy Birthday!"
                        f"\n\n {letter}")

send_email()