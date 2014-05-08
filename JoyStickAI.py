import win32com.client
import time
import serial

arduino = serial.Serial('COM9',9600)
shell = win32com.client.Dispatch("WScript.Shell")

delay = int(raw_input("Enter delay: "))

while True:
    if (arduino.read() == '0'):
        time.sleep(delay)
        shell.sendKeys(" ")
        arduino.flushInput()
        
    elif (arduino.read() == '1'):
        time.sleep(delay)
        shell.sendKeys("{RIGHT}")
        arduino.flushInput()
        
    elif (arduino.read() == '2'):
        time.sleep(delay)
        shell.sendKeys("{LEFT}")
        arduino.flushInput()
        
    elif (arduino.read() == '3'):
        time.sleep(delay)
        shell.sendKeys("{DOWN}")
        arduino.flushInput()
        
    elif (arduino.read() == '4'):
        time.sleep(delay)
        shell.sendKeys("{UP}")
        arduino.flushInput()

    time.sleep(0.05)

arduino.close()
