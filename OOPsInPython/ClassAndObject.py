class Computer:

    def config(self):
        print("i7, 16gb, 1TB")


# Object
com1 = Computer()
com2 = Computer()

# 1st way to call method
Computer.config(com1)
Computer.config(com2)

# 2nd way to call a method
com1.config()
com2.config()

