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
    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):
        for i in range(c.sim_iterations):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            time.sleep(1/60)
            # print(i)
    
    def __del__(self):
        p.disconnect()
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()