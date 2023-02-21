import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as numpy

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)