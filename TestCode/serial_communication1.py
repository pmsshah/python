#!/usr/bin/env python3
"""
File:          serial_communicator.py
Author:        Piyush Shah
Last Modified: Piyush on 5/2
"""

import serial
import time

port = "COM5"
baud = 9600
ser = None

def handel_feedback (data):
    dataarr = data[1:-3].split(",")
    for x in dataarr:
        try:
            val = float(x)
        except ValueError:
            val = None
        print(val)

def serial_open():
    ser = serial.Serial(port, baud, timeout=0.5)
    ser.close()
    ser.open()
    if ser.isOpen():
        print(ser.name + ' is open...')
    else:
        print("serial open error.")
        ser = None
    return ser

def serial_close():
    if ser == None or ser.isOpen == False: return;
    ser.close()


def serial_read(ser):
    if ser == None or ser.isOpen == False: return;
    feedback_str = ""
    while True:
        cmd = input("Enter command or 'exit':")
        if cmd == 'exit':
            ser.close()
            exit()
        else:
            print('sending: ', '<'+cmd+'>')
            barr1=('<'+cmd+'>').encode()
            ser.write(barr1)
            while ser.in_waiting > 0 or not feedback_str:
                feedback_str += ser.read().decode()
                print('==>', feedback_str)
            handel_feedback(feedback_str)
            feedback_str = ""

def serial_read1(ser, cmd1):
    if ser == None or ser.isOpen == False: return;
    feedback_str = ""
    while True:
        cmd = input("Enter command or 'exit':")
        if cmd == 'exit':
            ser.close()
            exit()
        else:
            print('sending: ', '<'+cmd+'>')
            barr1=('<'+cmd+'>').encode()
            ser.write(barr1)
            timeout = 10000 * 0.001
            tic = time.time()
            toc = time.time()
            i=0
            while toc - tic < timeout:
                i+=1
                bytesToRead = ser.inWaiting()
                bytesToWrite = ser.out_waiting
                feedback_str += ser.read(bytesToRead).decode()
                print('==>', i, bytesToRead, bytesToWrite, feedback_str)
                toc = time.time()
                if(feedback_str.endswith('>\r\n')): break
            handel_feedback(feedback_str)
            feedback_str = ""

def serial_read2(ser, cmd):
    if ser == None or ser.isOpen == False: return;
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    feedback_str = ""
    print('sending: ', '<'+cmd+'>')
    barr1=('<'+cmd+'>').encode()
    ser.write(barr1)
    ser.flush()
    timeout = 10000 * 0.001
    tic = time.time()
    toc = time.time()
    i=0
    while toc - tic < timeout:
        i+=1
        bytesToRead = ser.inWaiting()
        feedback_str += ser.read(bytesToRead).decode()
        print('==>', i, bytesToRead, feedback_str)
        toc = time.time()
        if(feedback_str.endswith('>\r\n')): break
    handel_feedback(feedback_str)
    feedback_str = ""

def serial_read3(ser, cmd):
    if ser == None or ser.isOpen == False: return;
    feedback_str = ""
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    print('sending: ', '<'+cmd+'>')
    barr1=('<'+cmd+'>').encode()
    ser.write(barr1)
    timeout = 10000 * 0.001
    tic = time.time()
    toc = time.time()
    while toc - tic < timeout:
        bytesToRead = ser.inWaiting()
        print('LoopSt:', ser.in_waiting, bytesToRead)
        feedback_str += ser.read(bytesToRead).decode()
        #print('LoopEnd', feedback_str)
        toc = time.time()
    print('LoopEnd', feedback_str)
    handel_feedback(feedback_str)
    feedback_str = ""

def serial_send_read(ser, cmd1):
    if ser == None or ser.isOpen == False: return;
    feedback_str = ""
    while True:
        #cmd = input("Enter command or 'exit':")
        if ser.in_waiting > 0:
            feedback_str += ser.read().decode()
            print('==>', feedback_str)
        elif not feedback_str:
            print('sending: ', '<'+cmd1+'>')
            barr1=('<'+cmd1+'>').encode()
            ser.write(barr1)
            #handel_feedback(feedback_str)
            #feedback_str = ""

ser = serial_open()
serial_read1(ser,"123")
serial_close()
#serial_send_read(ser, "123")
#handel_feedback("<123,xyz>")