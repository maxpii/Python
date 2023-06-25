# import random
# class Player:
#     def __init__(self, name, greeting):
#         self.name = name
#         self.greeting = greeting
#         self.guess = None
#
#     def makeGuess(self, guess):
#         self.guess = guess
#
#     def getGuess(self):
#         if self.guess == None:
#             return "No guess found"
#         return self.guess
#
#
# class Game:
#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2
#         self.board = [[-1, -1, -1] for i in range(3)]
#
#     def getBoard(self):
#         return self.board
#     def showBoard(self):
#         for i in self.board:
#             for j in i:
#                 print(j,end=" ")
#             print()
#     def playGame(self):
#         while not condition(self.board):
#         x_row = random.randint(0,2)
#         y_row = random.randint(0,2)
#         x_col = random.randint(0,2)
#         y_col = random.randint(0,2)
#     def condition(self):
#         if
#
# new_game = Game("Hanu", "manu")
# new_game.showBoard()