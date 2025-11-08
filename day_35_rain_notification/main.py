import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()
api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_FROM")
to_number = os.getenv("TWILIO_TO")

# define parameters for the OpenWeatherMap API request
parameters = {
    "lat": 50.0755,
    "lon": 14.4378,
    "appid": api_key,
    "cnt": 4 # number of forecast entries to check
}

# make the API call to retrieve the forecast data
response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
# raise an error if the request fails
response.raise_for_status()
# convert the API response from JSON text to a Python dictionary
data = response.json()

# check the weather codes in the forecast. IDs below 700 indicate rain, drizzle, snow, or other precipitation.
# check the first 4 forecast entries for any rain condition.
will_rain = any(item["weather"][0]["id"] < 700 for item in data["list"][:4])

# if rain is predicted and all Twilio credentials work, send a Whatsapp message
if will_rain and account_sid and auth_token and from_number and to_number:
    client = Client(account_sid,auth_token)
    message = client.messages \
    .create(
        body="Hey there. It's gonna rain today!",
        from_= from_number,
        to= to_number
    )
    # print the message SID for confirmation
    print(message.sid)
else:
    # otherwise print a fallback message if no rain forecast of credentials are missing
    print("No rain detected, or missing credentials/numbers.")