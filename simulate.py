from simulation import SIMULATION

# sim_iterations = 1000

# backLegSensorValues = numpy.zeros(sim_iterations)

# targetAnglesBackLeg = numpy.linspace(-2*numpy.pi, 2*numpy.pi, sim_iterations)
# targetAnglesBackLeg = c.amplitudeBackLeg * numpy.sin(c.frequencyBackLeg * targetAnglesBackLeg + c.phaseOffsetBackLeg)

# targetAnglesFrontLeg = numpy.linspace(-2*numpy.pi, 2*numpy.pi, sim_iterations)
# targetAnglesFrontLeg = c.amplitudeFrontLeg * numpy.sin(c.frequencyFrontLeg * targetAnglesFrontLeg + c.phaseOffsetFrontLeg)
# # numpy.save("data/targetAnglesBackLeg.npy", targetAnglesBackLeg)
# # numpy.save("data/targetAnglesFrontLeg.npy", targetAnglesFrontLeg)

# for i in range(sim_iterations):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")


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



#     time.sleep(1/60)
#     #print(i)

# numpy.save("data/backLegSensorValues.npy", backLegSensorValues)

# print(backLegSensorValues)

# p.disconnect()

simulation = SIMULATION()

simulation.Run()