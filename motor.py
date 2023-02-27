import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as numpy
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
    

    def Set_Value(self, desiredAngle, robotId):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce = 500)