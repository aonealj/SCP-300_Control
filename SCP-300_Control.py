# control functions for SCP-300 spin coater
import serial
import time

# establish
print('Establishing Serial Connection')
spin_coater = serial.Serial()
spin_coater.port = 'COM1'  # update port based on what shows up in device manager
spin_coater.baudrate = 19200  # default baud rate for SCP-300
spin_coater.timeout = 5  # sec
spin_coater.write_timeout = 5  # sec
spin_coater.open()  # important as port is not opened by default

if spin_coater.isOpen():
    print('Spin Coater Connection Open')
else:
    print('Spin Coater Connection Failed')


# functions to operate the equipment:

def cmd_sc(input_char):
    return bytes(str(input_char) + '\r\n', 'ascii')


# define a program to startup the connection with the motor
com_delay = 0.25  # seconds


def motor_startup(PWM=110, slope=950, intercept=550):
    # default values provided from in SCP documentation
    # set motor Pulse Width Modulation (PWM)
    spin_coater.write(cmd_sc('SetStartPWM,' + str(PWM)))
    time.sleep(com_delay)  # seconds. Pause program to ensure clean coms. Might be able to be shorter.

    # set motor profile slope
    spin_coater.write(cmd_sc('SetSlope,' + str(slope)))
    time.sleep(com_delay)

    # set motor profile intercept
    spin_coater.write(cmd_sc('SetIntercept,' + str(intercept)))
    time.sleep(com_delay)

    # turn on the motor
    spin_coater.write(cmd_sc('BLDCon'))
    time.sleep(com_delay)

    print('Spin Coater Motor Startup Complete')


# function to set the motor speed
def set_speed(rpm):
    spin_coater.write(cmd_sc('SetRPM,' + str(rpm)))


# motor speed will remain constant until changed


# function to query the motor for it's speed
def get_speed():
    spin_coater.write(cmd_sc('GetRPM'))
    current_speed = spin_coater.read_until(bytes('\n\r', 'ascii'))
    print(current_speed.decode())


# function to turn off the motor
def motor_shutoff():
    set_speed(0)
    time.sleep(5)
    spin_coater.write(cmd_sc('BLDCoff'))


# Setting slope for slower spin
# unsure about this, but seems to match documentation
def set_slope(slope):  # rpm/s, suspected
    slope_times_100 = slope * 100
    spin_coater.write(cmd_sc('SetSlope ' + str(slope_times_100)))
    print('Slope is now ' + str(slope))


# Check and update the status of the spin coater speed
def check_speed(duration, time_between):  # duration in seconds
    start = time.time()
    end = time.time()

    while (end - start) < duration:
        get_speed()
        time.sleep(time_between)
        end = time.time()

        # failsafe to prevent endless loops
        i = 0
        i += 1
        if i > 1000:
            break

