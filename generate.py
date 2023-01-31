import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 1
y = 1
z = 0.5

pyrosim.Start_SDF("boxes.sdf")

for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x,y,z + i] , size=[length, width, height])

pyrosim.End()