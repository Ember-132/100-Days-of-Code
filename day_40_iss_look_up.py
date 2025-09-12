import requests
import datetime as dt
import smtplib
import time

# your location you want to check
LAT = 40.9006
LONG = 174.8860

# your email and password
EMAIL = "xxx"
PASSWORD = "xxx"

def iss_above():
    '''checks if the IIS satellite is above your location'''
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_long = float(data['iss_position']['longitude'])
    iss_lat = float(data['iss_position']['latitude'])

    if LONG - 5 <= iss_long <= LONG + 5 and LAT - 5 <= iss_lat <= LAT + 5:
        return True

def is_night():
    '''checks if it's night time'''
    parameters = {
        "lat": LAT,
        "lng": LONG,
        "formatted": 0
    }
    new_response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    new_response.raise_for_status()
    sun_data = new_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    today = dt.datetime.today()
    hour = today.hour

    if sunset <= hour <= sunrise:
        return True

while True:
    # if the satellite is above you and it is night time, send the message to look up
    if iss_above() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as communication:
            communication.starttls()
            communication.login(user=EMAIL, password=PASSWORD)
            communication.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="IMPORTANT\n\nLook up!"
            )
    # wait an hour until the next message is sent
    time.sleep(3600)
