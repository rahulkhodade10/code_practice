class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
     print("config is ",self.cpu, self.ram)



# Object
com1 = Computer('i5',8)
com2 = Computer('Ryzen 3',8)


com1.config()
com2.config()