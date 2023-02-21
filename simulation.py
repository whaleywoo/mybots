from robot import ROBOT
from world import WORLD

import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time as time
import numpy as numpy
import random as random
import constants as c

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.sim_iterations):
            p.stepSimulation()
            self.robot.Sense(i)


        #     pyrosim.Set_Motor_For_Joint(
        #     bodyIndex = robotId,
        #     jointName = b'Torso_BackLeg',
        #     controlMode = p.POSITION_CONTROL,
        #     targetPosition = targetAnglesBackLeg[i],
        #     maxForce = 500)

        #     pyrosim.Set_Motor_For_Joint(
        #     bodyIndex = robotId,
        #     jointName = b'Torso_FrontLeg',
        #     controlMode = p.POSITION_CONTROL,
        #     targetPosition = targetAnglesFrontLeg[i],
        #     maxForce = 500)



            time.sleep(1/60)
            print(i)
    
    def __del__(self):
        p.disconnect()