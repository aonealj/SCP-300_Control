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

Designed for windows computers. If other OS used, update COM port assignment