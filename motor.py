import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as numpy
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg

        
        if self.jointName == b'Torso_BackLeg':
            self.frequency /= 2


        self.targetAngles = numpy.linspace(-2*numpy.pi, 2*numpy.pi, c.sim_iterations)
        self.targetAngles = self.amplitude * numpy.sin(self.frequency * self.targetAngles + self.offset)
    

    def Set_Value(self, t, robotId):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = self.targetAngles[t],
        maxForce = 500)
    

    def Save_Values(self):
        numpy.save("data/" + self.jointName + "MotorValues.npy", self.targetAngles)