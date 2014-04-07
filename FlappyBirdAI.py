import win32com.client
import time
import serial

arduino = serial.Serial('COM9',9600)
shell = win32com.client.Dispatch("WScript.Shell")

while True:
    if (arduino.read() == '1'):
        time.sleep(0.1)
        shell.sendKeys(" ")
        arduino.flushInput()

arduino.close()
