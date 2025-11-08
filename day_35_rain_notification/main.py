import requests
from twilio.rest import Client
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

api_key = "77276c1d5821678ce5640e5d337c6c9e"
account_sid = "AC61280fe3c1b6cd61e18432f6c07eb8e0"
auth_token = "c0c87f141d9f167e72f94254d29a14ee"
parameters = {
    "lat": 50.733810,
    "lon": -1.776020,
    "appid": api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
numbers = [data["list"][index]["weather"][0]["id"] for index in range(0,4)]
for item in numbers:
    if item < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
    .create(
        body="Hey there. It's gonna rain today!",
        from_='whatsapp:+14155238886',
        to='whatsapp:+447583378041'
    )
    print(message.sid)
    