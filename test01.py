#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
from time import sleep

import serial

connected = False


def sendPrinter(ser: serial, in_text=b''):
    ser.write(in_text + b'\r\n')
    while 1:
        line = ser.readline()
        if line:
            print(line)
        if line == b'wait\r\n':
            break
        # if line == b'ok 0\r\n':
        #     break


# ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
with serial.Serial('/dev/ttyUSB0', 115200, bytesize=8, parity='N', stopbits=1, timeout=10.0, xonxoff=False,
                   rtscts=False, dsrdtr=False) as ser:
    line = ser.readline()  # read a '\n' terminated line


    # if (line == b"start\r\n"):
    #     print(line)
        # sendPrinter(ser, b'M999')
    sendPrinter(ser, b'M115')
    # sendPrinter(ser, b'G28')
    # sendPrinter(ser, b'M106')
    # sendPrinter(ser, b'M107 P4')
    # sendPrinter(ser, b'M909')
    # sendPrinter(ser, b'M18 S60')
    # sendPrinter(ser, b'M20')
    # sendPrinter(ser, b'')
    # sendPrinter(ser, b'')
    # sendPrinter(ser, b'')
    # sendPrinter(ser, b'')

