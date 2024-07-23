import requests
import os
from twilio.rest import Client


api_key = os.environ.get("OWM_APY_KEY")
account_sid = os.environ.get("ACCOUNT_APY_KEY")
auth_token = os.environ.get("AUTH_APY_KEY")


parameters = {
    "lat": 43.451637,
    "lon": -80.492531,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_id_list = []

for data_id in weather_data["list"]:
    weather_id_list.append(data_id["weather"][0]["id"])

need_umbrella = all(num for num in weather_id_list if num < 700)
if need_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="I can see you",
        from_='+OUR_NUMBER',
        to='+MY_NUMBER'
    )
    print(message.status)

