class Skylander:

    def __init__(self,Name:str,exp:int,Level:int,gold:int,gimmick:str):
        self.Name = Name
        self.Level = Level
        self.gold = gold
        self.gimmick = gimmick

        def kill_enemy(self,amount:int):
            self.exp += amount
            if self.exp >= 1000 and self.Level < 15:
                while self.exp >= 1000:
                    Level += 1
                    print(f"{self.Name} leveled up to level {self.Level}")
                    self.exp -= 1000
            else:
                print(f"{self.Name} cannot level up further!")

        def collect_gold(self,money_collected:int):
            if self.gold < 65536:
                print(f"{self.Name} has collected gold!")
                self.gold += money_collected
                if self.gold > 65536:
                    self.gold = 65536

        def solve_lock(self):
            print(f"{self.Name} solved a Lock Puzzle!")

        def rest(self):
            print(f"{self.Name} needs to rest.")

        def read_stats(self):
            print(f"{self.Name} is a level {self.level} {gimmick} skylander with {self.exp} exp, and {self.gold} gold")
            
                