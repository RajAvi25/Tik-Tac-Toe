import os
import numpy as np

os.system("cls")


class Board():
    def __init__(self) -> None:
        self.values = np.full((9,)," ") 

    def display(self):
        os.system("cls")
        print(" ")
        print(" {} | {} | {}".format(self.values[0],self.values[1],self.values[2]))
        print("----------")
        print(" {} | {} | {}".format(self.values[3],self.values[4],self.values[5]))
        print("----------")
        print(" {} | {} | {}".format(self.values[6],self.values[7],self.values[8]))

    def calculateIndex(self,row,column):
        if row == 1 and column == 1:
            return 0
        if row == 1 and column == 2:
            return 1
        if row == 1 and column == 3:
            return 2
        if row == 2 and column == 1:
            return 3
        if row == 2 and column == 2:
            return 4
        if row == 2 and column == 3:
            return 5
        if row == 3 and column == 1:
            return 6
        if row == 3 and column == 2:
            return 7
        if row == 3 and column == 3:
            return 8
    
    def move(self,row,column,player):
        idx = self.calculateIndex(row,column)
        if player ==1:
            self.values[idx]="X"
        elif player ==2:
            self.values[idx]="O"
        else:
            raise ValueError("Invalid player")
        self.display()
        if self.checkWinner():
            print("You Won!")
    def checkWinner(self):
        self.rows = np.array([[self.values[0],self.values[1],self.values[2]],[self.values[3],self.values[4],self.values[5]],
                     [self.values[6],self.values[7],self.values[8]]]).copy()
        self.columns = np.array([[self.values[0],self.values[3],self.values[6]],[self.values[1],self.values[4],self.values[7]],
                     [self.values[2],self.values[5],self.values[8]]]).copy()  
        self.diagonals = np.array([[self.values[0],self.values[4],self.values[8],],[self.values[2],self.values[4],self.values[6]]]).copy()

        compare_fn = np.vectorize(lambda x: x != " ")
        
        for row in self.rows:
            if all(row[1:] == row[:-1]) and all(compare_fn(row[1:])):
                return True
        for column in self.columns:
            if all(column[1:] == column[:-1]) and all(compare_fn(column[1:])):
                return True
        for diagonal in self.diagonals:
            if all(diagonal[1:] == diagonal[:-1]) and all(compare_fn(diagonal[1:])):
                return True

        return False
    def gameOver(self):
        if all(self.values != " "):
            return True
        else:
            return False
        
board = Board()
board.display()
# board.move(1,1,2)
# board.move(2,1,1)
# board.move(3,1,1)

while True:
    response = input("Make your move: ")

    if response == "Q" or response== "q":
            break 
    
    elif response[1] != "," and response[3] != ",":
        print("Invalid response")

    elif len(response) != 5:
        print("Invalid response") 

    else:
        move = tuple(map(int, response.split(',')))
        if move[0] < 1 or move[0] > 3 or move[1] < 1 or move[1] > 3 or move[2] < 1 or move[2] > 2:
            print("Invalid response")
            continue
        board.move(*move)
        if board.gameOver():
            print("Game Over!")
            break

