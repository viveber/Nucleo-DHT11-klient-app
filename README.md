# The program for the operetion of STM32 Nucleo F401RE platform with DHT-11 sensor
## Bin file
Use [this files](https://github.com/viveber/Nucleo-DHT11-klient-app/tree/master/DHT11(mbed%20files)) in ide.mbed.com to create bin file for Nucleo.

Use some kind of terminal (like terra term) to check if it works.

![terminal](https://github.com/viveber/Nucleo-DHT11-klient-app/blob/master/pics/terminal.png)

## Saving information
Run nucleo.py for saving information into csv.

## Visualization
Python web app for visuzlisation: app.py (it has auth form, login and password in login.txt)

![app](https://github.com/viveber/Nucleo-DHT11-klient-app/blob/master/pics/app.png)
![auth](https://github.com/viveber/Nucleo-DHT11-klient-app/blob/master/pics/auth.png)

App also has notification function: smtp-alert.py

![notif](https://github.com/viveber/Nucleo-DHT11-klient-app/blob/master/pics/notifications.png)
