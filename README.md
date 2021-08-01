# SCP-300_Control
Python program for running Intras SCK-300P from a computer or integrations into larger programs.

Connection to the spin coater is achieved using a standard USB to UART cable, connecting GND TXD and RXD cables to the 
pins on the MiM. Do NOT connect the voltage cable. Connection will require the MiM to be removed from the base and, 
depending on the cable size, the MiM may not fit back against the base with the cables installed. Also, it is important 
to remember that the TXD and RXD cables should be connected to the opposite labeled pins based on the standards of serial 
communication.

Python libraries required:
1. PySerial
2. Time

Designed for Windows computers. If other OS used, update COM port assignment. Mac and Linux OS use different syntax from 
Windows, so the COM port nomenclature will need to be changed.

Full list of possible commands available at https://gist.github.com/ns96/ef95fd06573a871adfa1c4bed21eef43
I've just put the useful ones here.

* cmd_spin_coater: turns a standard string into the correct ascii string with ending return.
* com_delay: short delay introduced to the code to allow for the coms to catch up with the running. Without this, code will skip.
* motor startup: sets the necessary defaults on the motor prior to setting any Set Point
    - PWM: pulse width modulation. Standard from spin coater documentation is 110
    - Slope: motor profile slope. Standard from spin coater documentation is 950
    - Intercept: spin coater motor profile intercept. Standard from spin coater documentation is 550.
    - BLDCon: Truns the motor on. Sleep time after this step may not be necessary
* set_speed: changes the Set Point (SP) for the motor speed. Motor speed remains constant until changed.
* get_speed: queries the motor to read the speed.
* motor_shutoff: turns the motor off
* set_slope: Set the ramp speed for the motor
* check_speed: check and return the speed of the motor for a set amount of time with a set interval. Time in seconds



The idea here is to use this as the basis of further code. Each of the functions can be copied into the code 
to allow for the development of a programmed protocol.