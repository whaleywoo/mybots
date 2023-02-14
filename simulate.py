import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time as time
import numpy as numpy
import random as random

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

sim_iterations = 1000

backLegSensorValues = numpy.zeros(sim_iterations)

targetAngles = numpy.linspace(-2*numpy.pi, 2*numpy.pi, sim_iterations)
targetAngles = numpy.sin(targetAngles) * numpy.pi/4
numpy.save("data/targetAngles.npy", targetAngles)

for i in range(sim_iterations):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")


    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_BackLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = random.uniform(-0.1, 0.1),
    maxForce = 500)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_FrontLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = random.uniform(-0.1, 0.1),
    maxForce = 500)



    time.sleep(1/60)
    #print(i)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)

print(backLegSensorValues)

p.disconnect()