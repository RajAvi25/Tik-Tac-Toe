from Board import *
# board = Board()

def minimax(board, depth, maximizingPlayer):
    node = board.values
    if depth == 0 or isTerminalNode(board):
        return heuristic(node), None

    if maximizingPlayer:
        bestValue = float('-inf')
        bestNode = None
        childrenNodes = Expand(node)
        for childNode in childrenNodes:
            value, _ = minimax(childNode, depth - 1, False)
            if value > bestValue:
                bestValue = value
                bestNode = childNode
        return bestValue, bestNode

    else:
        bestValue = float('inf')
        bestNode = None
        childrenNodes = Expand(node)
        for childNode in childrenNodes:
            value, _ = minimax(childNode, depth - 1, True)
            if value < bestValue:
                bestValue = value
                bestNode = childNode
        return bestValue, bestNode


def isTerminalNode(board):
    if board.checkWinner() or board.gameOver():
        return True
    else:
        return False
    
def Expand(node,player):
    children = []
    for i in range(len(node)):
        if node[i] == " ":
            # Create a copy of the current node
            child = node.copy()
            if player:
                # Update the copy with the new move
                child[i] = "X"  # Assuming "X" is the maximizing player's move
                children.append(child)
            else:
                child[i] = "O"  # Assuming "O" is the maximizing player's move
                children.append(child)
    return children


def heuristic(_node):
    pass


