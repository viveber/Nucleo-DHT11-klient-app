import serial
import datetime
from datetime import date
import csv

# COM port config
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    timeout=None,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ser.isOpen()

# получение данных с COM3 и запись в файлы
while True :
    out = ser.readline()
    out = out.decode()
    current_date = date.today()
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    if "T" in out:
        temp = out[5] + out[6]
        with open("temp.csv", mode="a", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow([current_date, current_time, temp])
    elif "H" in out:
        hum = out[4] + out[5]
        with open("hum.csv", mode="a", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow([current_date, current_time, hum])
    
