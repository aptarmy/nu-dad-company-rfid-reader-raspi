#!/usr/bin/python

import serial
import time

ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate=9600
)

try:
	while True:
		print("writing data.")

		ser.write(b"hello world")
		time.sleep(1)

except Exception as e:
	print(e)
	ser.close()
