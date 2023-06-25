class Player:
    num_of_players = 0
    def __init__(self,name,dribbling,shooting):
        self.name = name
        self.dribbling = dribbling
        self.shooting = shooting
        Player.num_of_players += 1
    def __add__(self, other):
        if type(other) is not Player:
            print("What are you trying to do?")
        else:
            new_name = self.name[:self.name.index(" ")] + " " + other.name[other.name.index(" ") + 1:]
            return Player(new_name, self.dribbling + other.dribbling, self.shooting + other.shooting)
    def __repr__(self):
        return f"Hi! My name is {self.name}. My shooting is {self.shooting} and my dribbling is {self.dribbling}"

    def getPassing(self):
        return self.passing
    def getDribbling(self):
        return self.dribbling
    def getShooting(self):
        return self.shooting
    @classmethod
    def getPlayerCount(cls):
        return cls.num_of_players
    @staticmethod
    def getGreatPlayers():
        for i in ["Lionel Messi", "Cristiano Ronaldo", "Muhammad Raza", "Muhammad Salah"]: print(i)
player1 = Player("Neymar Jr.",85,15)
player2 = Player("Cristiano Ronaldo",75,25)
player1 += player2
print(player1.name)


