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

        pyrosim.Prepare_To_Simulate(robotId)