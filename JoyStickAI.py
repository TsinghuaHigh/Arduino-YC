import win32com.client
import time
import serial

arduino = serial.Serial('COM9',9600)
shell = win32com.client.Dispatch("WScript.Shell")

while True:
    if (arduino.read() == '0'):
        time.sleep(0.1)
        shell.sendKeys(" ")
        arduino.flushInput()
    #endif
        
    if (arduino.read() == '1'):
        time.sleep(0.1)
        shell.sendKeys("{RIGHT}")
        arduino.flushInput()
    #endif
        
    if (arduino.read() == '2'):
        time.sleep(0.1)
        shell.sendKeys("{LEFT}")
        arduino.flushInput()
    #endif
        
    if (arduino.read() == '3'):
        time.sleep(0.1)
        shell.sendKeys("{DOWN}")
        arduino.flushInput()
    #endif
        
    if (arduino.read() == '4'):
        time.sleep(0.1)
        shell.sendKeys("{UP}")
        arduino.flushInput()
    #endif

    time.sleep(0.1)

arduino.close()
