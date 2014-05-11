import win32com.client
import time
import serial

arduino = serial.Serial('COM9',9600)
shell = win32com.client.Dispatch("WScript.Shell")

delay = int(raw_input("Enter delay: "))

while True:
    if (arduino.read() == '1'):
        time.sleep(delay)
        shell.sendKeys(" ")
        arduino.flushInput()

arduino.close()
