import win32com.client
import time
import serial

shell = win32com.client.Dispatch("WScript.Shell")

delay = float(raw_input("Enter delay: "))

RIGHT = '1'
LEFT = '2'
DOWN = '3'
UP = '4'
END = '0'

while True:
    arduino = serial.Serial('COM9',9600)
    mode = int(raw_input("Choose a mode(0 for JS, 1 for FB): "))
    
    while True:
        if (arduino.inWaiting() != '0'):    
            if (arduino.read() == RIGHT):
                time.sleep(delay)
                shell.sendKeys("{RIGHT}")
                print "RIGHT"
                arduino.flushInput()
                
            elif (arduino.read() == LEFT):
                time.sleep(delay)
                shell.sendKeys("{LEFT}")
                print "LEFT"
                arduino.flushInput()
                
            elif (arduino.read() == DOWN):
                time.sleep(delay)
                shell.sendKeys("{DOWN}")
                print "DOWN"
                arduino.flushInput()
                
            elif (arduino.read() == UP):
                time.sleep(delay)
                if (mode == 0):
                    shell.sendKeys("{UP}")
                    print "UP"
                else:
                    shell.sendKeys(" ")
                    print "SPACE"
                arduino.flushInput()
                
            elif (arduino.read() == END):
                time.sleep(delay)
                print "END"
                break
                
    arduino.close()
