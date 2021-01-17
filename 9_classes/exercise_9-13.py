from random import randint

class Die():

    def __init__(self, sides=6):

        self.sides = sides
    
    def roll_die(self):
        print(randint(1,self.sides + 1))

my_die = Die()
for i in range(10):
    my_die.roll_die()

ten_die = Die(10)
for i in range(10):
    ten_die.roll_die()

twenty_die = Die(20)
for i in range(10):
    twenty_die.roll_die()
