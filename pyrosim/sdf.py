class SDF:

    def __init__(self):

        self.depth = 0

    def Save_Start_Tag(self,f):

        f.write('<sdf><world>\n')

    def Save_End_Tag(self,f):

        f.write("</world></sdf>")
