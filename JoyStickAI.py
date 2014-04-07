import win32com.client
import time
import serial

arduino = serial.Serial('COM9',9600)
shell = win32com.client.Dispatch("WScript.Shell")

while True:
    if (arduino.read() == '0'):
        time.sleep(0.25)
        shell.sendKeys("{RIGHT}")
        arduino.flushInput()
    if (arduino.read() == '1'):
        time.sleep(0.25)
        shell.sendKeys("{LEFT}")
        arduino.flushInput()
    if (arduino.read() == '2'):
        time.sleep(0.25)
        shell.sendKeys("{DOWN}")
        arduino.flushInput()
    if (arduino.read() == '3'):
        time.sleep(0.25)
        shell.sendKeys("{UP}")
        arduino.flushInput()

arduino.close()
