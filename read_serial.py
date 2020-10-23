#!/usr/bin/python

import serial
import time
from datetime import datetime

ser = serial.Serial(
	port="/dev/ttyAMA0",
	baudrate=9600
)


try:
	readedData = ""
	isReading = True

	while True:

		while(ser.inWaiting() > 0):
			char = str(ser.read())
			if ord(char) == 2: isReading = True;
			if ord(char) == 3: isReading = False;
#			print("> '{}', type: {}, ASCII: {}".format(char, type(char), ord(char)))

			if isReading == False: break;
			if ord(char) != 2 and ord(char) != 3:
				readedData += char
			time.sleep(0.01)

		if readedData != "" and len(readedData) == 12:
			print("{} READ >>> {}".format(datetime.now(), readedData))

		if readedData != "" and len(readedData) != 12:
			print("{} ERR  >>> {}".format(datetime.now(), readedData))

		readedData = ""
		time.sleep(0.01)


except Exception as e:
	ser.close()
	print(e)
