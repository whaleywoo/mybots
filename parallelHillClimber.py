from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION()
    
    def Evolve(self):
        for i in range(c.populationSize):
            self.parents[i].Evaluate("GUI")
        
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        pass

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate("DIRECT")

        self.Print()

        self.Select()

    def Print(self):
        print("Parent fitness: " + self.parent.fitness + ", Child fitness: " + self.child.fitness)
    
    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass