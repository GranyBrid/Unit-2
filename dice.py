import random

class Die():
    def __init__(self, sides: int = 6):
        self.sides = sides

    def roll_die(self):
        roll = random.randint(1,self.sides)
        print(roll)

def lotto():
    list = ["5","4","6","3","7","2","8","1","9","10","S","I","G","M","A"]

    digit1 = random.randint(0,14)
    digit2 = random.randint(0,14)
    digit3 = random.randint(0,14)
    digit4 = random.randint(0,14)
    print(f"Any ticket with the numbers {digit1}, {digit2}, {digit3}, and {digit4} win a prize!")
        
        

def main():
    D6 = Die(6) 
    D10 = Die(10)
    D20 = Die(20)
    """for i in range(10):
        D6.roll_die()
        D10.roll_die()
        D20.roll_die()"""

if __name__ == "__main__":
    main()