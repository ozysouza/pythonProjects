import os
import requests
import smtplib as mail
import time

from datetime import datetime

SENDER = "ozysouzaa@gmail.com"
RECEIVER = "ozysouza@hotmail.com"
PASSWD = "xxequcbfdzrjqayl"
MY_LAT = -1.8920
MY_LONG = 159.2561
TOLERANCE = 5


def is_iss_visible():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    is_close = all([
        MY_LAT - TOLERANCE <= iss_latitude <= MY_LAT + TOLERANCE,
        MY_LONG - TOLERANCE <= iss_longitude <= MY_LONG + TOLERANCE,
    ])

    if is_close:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now < sunrise or time_now >= sunset:
        return True


def send_email():
    with mail.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER, password=PASSWD)
        connection.sendmail(
            from_addr=SENDER,
            to_addrs=RECEIVER,
            msg="Subject:ISS Is Visible!"
                f"\n\n Hey! The ISS is visible, go check it out!")


while True:
    time.sleep(60)
    if is_iss_visible() and is_night():
        send_email()
