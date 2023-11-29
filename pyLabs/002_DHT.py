import time
import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 4
while True:
    try:
        h ,t = Adafruit_DHT.read_retry(sensor, pin)
        if h is not None and t is not None:
            print("Temperature = {0:0.2f}*C, Humidity = {1:0.2f}%".format(t,h))
        else :
            print("Read error")
        time.sleep(2)
    except KeyboardInterrupt:
        pass
        print("Exit")
        exit()