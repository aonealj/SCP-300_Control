# control functions for SCP-300 spin coater
import serial
import time


# establish
print('Establishing Serial Connection')
sc = serial.Serial()
sc.port = 'COM1'        # update port based on what shows up in device manager
sc.baudrate = 19200     # default baud rate for SCP-300
sc.timeout = 5          # sec
sc.write_timeout = 5    # sec
sc.open()               # important as port is not opened by default


# functions to operate the equipment


def cmdsc(inputChar):
    stringInput = str(inputChar) + '\r\n'
    return bytes(stringInput, 'ascii')

# define a program to startup the connection with the motor
def motorStartup(PWM=110, slope=950, intercept=550):
    # set motor Pulse Width Modulation (PWM)
    PWMstr = 'SetStartPWM,' + str(PWM)
    PWMin = cmdsc(PWMstr)
    sc.write(PWMin)
    time.sleep(1)                       # pause program to ensure clean coms. Might be able to be shorter.

    # set motor profile slope
    slopeStr = 'SetSlope,' + str(slope)
    slopeIn = cmdsc(slopeStr)
    sc.write(slopeIn)
    time.sleep(1)

    # set motor profile intercept
    intStr = 'SetIntercept,' + str(intercept)
    intIn = cmdsc(intStr)
    sc.write(intIn)
    time.sleep(1)

    # turn on the motor
    onCmd = 'BLDCon'
    onCmdByt = cmdsc(onCmd)
    sc.write(onCmdByt)
    time.sleep(1)

    print('Spin Coater Motor Startup Complete')


# function to set the motor speed
def setSpeed(rpm):
    rpmStr = 'SetRPM,' + str(rpm)
    rpmIn = cmdsc(rpmStr)
    sc.write(rpmIn)


# function to query the motor for it's speed
def getSpeed():
    getSpeed = cmdsc('GetRPM')
    sc.write(getSpeed)
    current_speed = sc.read_until(bytes('\n\r', 'ascii'))
    print(current_speed.decode())


# function to turn off the motor
def motorShutoff():
    setSpeed(0)
    time.sleep(5)
    sc.write(cmdsc('BLDCoff'))

