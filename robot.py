import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import numpy as numpy
import os

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, solutionID):
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        os.system("del brain" + str(solutionID) + ".nndf")
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)


    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)


    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)
    

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()
    
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("fitness.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()