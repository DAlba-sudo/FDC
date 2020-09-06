from sensors import Translater
from time import sleep

def get_code():
    while True:
        if com.communicator.in_waiting > 0:
            code = com.communicator.read(3).decode("utf-8").rstrip()
            return code

if __name__ == "__main__":
   
    # Establish Connection
    com = Translater(9600, 1)
    com.communicator.flush()
    com.communicator.write("250".encode("utf-8"))
    
    # Get Response
    response = get_code()
    if(response is not "200"):
       raise Exception("There is no Arduino! Connection can not be Established!")
    else:
        pass

    # Create LoadCell
    com.communicator.write("301".encode("utf-8"))
    response = get_code()
    if(response is not "200"):
        raise Exception("Arduino could not successfully connect to the LoadCell")

    # Entering Feedback Loop
    while True:
        sleep(1)
        com.communicator.write("302".encode("utf-8"))
        response = get_code()
        if(response is not "200"):
            raise Exception("Arduino could not successfully connect to the LoadCell")
        else:
            print("We got some data!")




   
   


