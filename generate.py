import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 1
y = 1
z = 0.5

pyrosim.Start_SDF("boxes.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
pyrosim.Send_Cube(name="Box2", pos=[2,1,1.5] , size=[length, width, height])
pyrosim.End()