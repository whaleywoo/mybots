import constants as c
import numpy as numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.sim_iterations)
    

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)