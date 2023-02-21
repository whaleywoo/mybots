import numpy as numpy
import matplotlib.pyplot as pyplot

# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
# print(backLegSensorValues)

# pyplot.plot(backLegSensorValues)

targetAnglesBackLeg = numpy.load("data/targetAnglesBackLeg.npy")
targetAnglesFrontLeg = numpy.load("data/targetAnglesFrontLeg.npy")

pyplot.plot(targetAnglesBackLeg)
pyplot.plot(targetAnglesFrontLeg)

pyplot.show()