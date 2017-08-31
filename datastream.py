#!/usr/local/bin/python

import pyrebase
from sense_hat import SenseHat
from datetime import datetime
from time import sleep

def main():
    config = {
      "apiKey": "AIzaSyBV6QxapT5wjitx939KUQLADEDscY6VvKM",
      "authDomain": "raspberrydashboard.firebaseapp.com",
      "databaseURL": "https://raspberrydashboard.firebaseio.com",
      "storageBucket": "raspberrydashboard.appspot.com",
      "serviceAccount": "secret.json"
    }

    firebase = pyrebase.initialize_app(config)
    sense = SenseHat()
    data = {}
    db = firebase.database()

    while True:
        data.temperature = sense.get_temperature()
        data.pressure    = sense.get_pressure()
        data.humidity    = sense.get_humidity()
        data.time        = datetime.now()

        db.child('datastream').push(data)
        sleep(60)

if __name__ == "__main__":
    main()
