# control functions for SCP-300 spin coater
import serial
import time

# establish
print('Establishing Serial Connection')
sc = serial.Serial()
sc.port = 'COM1'  # update port based on what shows up in device manager
sc.baudrate = 19200  # default baud rate for SCP-300
sc.timeout = 5  # sec
sc.write_timeout = 5  # sec
sc.open()  # important as port is not opened by default

if sc.isOpen() == True:
    print('Spin Coater Connection Open')
else:
    print('Spin Coater Connection Failed')


# functions to operate the equipment

# function to create cmd signal with byes and end chars from string input
def cmd_sc(inputChar):
    return bytes(str(inputChar) + '\r\n', 'ascii')


# define a program to startup the connection with the motor
com_delay = 0.25  # seconds


def motor_startup(PWM=110, slope=950, intercept=550):
    # default values provided from in SCP documentation
    # set motor Pulse Width Modulation (PWM)
    sc.write(cmd_sc('SetStartPWM,' + str(PWM)))
    time.sleep(com_delay)  # seconds. Pause program to ensure clean coms. Might be able to be shorter.

    # set motor profile slope
    sc.write(cmd_sc('SetSlope,' + str(slope)))
    time.sleep(com_delay)

    # set motor profile intercept
    sc.write(cmd_sc('SetIntercept,' + str(intercept)))
    time.sleep(com_delay)

    # turn on the motor
    sc.write(cmd_sc('BLDCon'))
    time.sleep(com_delay)

    print('Spin Coater Motor Startup Complete')


# function to set the motor speed
def set_speed(rpm):
    sc.write(cmd_sc('SetRPM,' + str(rpm)))
# motor speed will remain constant until changed


# function to query the motor for it's speed
def get_speed():
    sc.write(cmdsc('GetRPM'))
    current_speed = sc.read_until(bytes('\n\r', 'ascii'))
    print(current_speed.decode())


# function to turn off the motor
def motor_shutoff():
    setSpeed(0)
    time.sleep(5)
    sc.write(cmd_sc('BLDCoff'))
