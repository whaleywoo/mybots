import numpy as numpy
import matplotlib.pyplot as pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
print(backLegSensorValues)

pyplot.plot(backLegSensorValues)

pyplot.show()