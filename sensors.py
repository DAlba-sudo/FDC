import serial

class Translater():

    def __init__(self, BAUDRATE, timeout):
        self.BAUDRATE = BAUDRATE
        self.TIMEOUT = timeout

        self.known_addresses = ["COM3", "/dev/ttyACM%s", "/dev/ttyUSB%s"]
        self.communicator = serial.Serial()

        arduino_connection = self.testConnections()

    def testConnections(self):
        # used for finding out if a connection is stable
        connection_found = False 
        partition = 0
        while not connection_found:
            for addr in range(len(self.known_addresses)):
                current_name = self.known_addresses[addr]
                if addr == 0:
                    try:
                        self.communicator = serial.Serial(port=current_name, baudrate=self.BAUDRATE, timeout=self.TIMEOUT)
                        connection_found = True
                        return current_name
                    except serial.SerialException:
                        partition += 1
                else:
                    try:
                        self.communicator = serial.Serial(port=current_name, baudrate=self.BAUDRATE, timeout=self.TIMEOUT)
                        connection_found = True
                        return current_name
                    except serial.SerialException:
                        partition += 1

class Sensor():
    def __init__(self, name):
        self.name = name
        self.arduino_port = None
    
    def link_port(self, port):
        self.arduino_port = port

    
