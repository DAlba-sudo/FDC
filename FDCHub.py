import serial
import serial.tools.list_ports
import time
import threading

CORRECT_NAME = "COM3"
CONNECTED = False
ARDUINO_PORT = None

myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]

def check_connection(correct_port, interval=0.1):
    while True:
        myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
        if arduino_port not in myports:
            # Raise a warning 
            CONNECTED = False
            break
        time.sleep(interval)

# Method for starting our port
def start_port(name, baud_rate):
    # If there is no error, we have the right port and thus we set the correct name
    try:
        # Create an instance of our serial object
        ser = serial.Serial(str(name), int(baud_rate), timeout=1)
        CORRECT_NAME = name # Used for referencing our correct port
        return ser # returns the object
    except serial.SerialException:
        print("There is no arduino here!")

def main():
    # Gets the right port
    try:
        ser = start_port("COM3", 9600)
    except SerialException:
        try:
            ser = start_port("/dev/ttyACM0", 9600)
        except serial.SerialException:
            try:
                ser = start_port("/dev/ttyUSB0", 9600)
            except serial.SerialException:
                print("None of the known ports contain an aruino!")
    
    ARDUINO_PORT = [port for port in myports if CORRECT_NAME in port][0]

    if ARDUINO_PORT is None:
        raise Exception("ARDUINO PORT is None")

    # Setting Daemon Thread for Detecting Arduino
    port_controller = threading.Thread(target=check_connection, args=(ARDUINO_PORT, 0.1,)) # may raise error due to ARDUINO PORT being None




if __name__ == '__main__':
    pass