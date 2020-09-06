class Sensor():
    
    def __init__(self, name):
        self.name = name
        self.INPUT = None
        self.time_list = []
        self.data_list = []
        self.DATA = {

        }
    
    def add_data(self, time, dta):
        self.time_list.append(time)
        self.data_list.append(dta)
        self.DATA[time] = dta
    
    def request_sensor(self):
        pass

class LoadCell(Sensor):
    def __init__(self, name):
        pass

    def set_INPUT(self):
        self.INPUT = 