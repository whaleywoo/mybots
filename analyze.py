import numpy as numpy
import matplotlib.pyplot as pyplot

# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
# print(backLegSensorValues)

# pyplot.plot(backLegSensorValues)

targetAngles = numpy.load("data/targetAngles.npy")
print(targetAngles)

pyplot.plot(targetAngles)

pyplot.show()