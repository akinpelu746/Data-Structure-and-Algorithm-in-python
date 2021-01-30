class Boardgame:
    def __init__(self, size):
        self.allowedMove = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.size = size
        self.array = self.boardArray()

    def move(self, currPosition):
        return [(currPosition[0] + i[0] ,currPosition[1] + i[1]) for i in self.allowedMove]

    def boardSize(self):
        return self.size

    def board(self):
        return self.array

    def boardArray(self):
        return [[0 for i in range(self.size[1])] for j in range(self.size[0])]

    def addOne(self, position):
        self.array[position[0]][position[1]] = 1

    # i need to add a function to add 1


def BFS(board, currPosition, size):
    movement = [currPosition]
    tmpPath = []
    boardplay = board.board()
    while len(movement) != 0:
        tmpPath.append(movement.pop(0))
        currPos = tmpPath[-1]
        if size[0] >= currPos[0] >= 0 and size[1] >= currPos[1] >= 0:

            if boardplay[currPos[0]][currPos[1]] == 1:
                return currPos

            newPositions = board.move(currPos)
            for newPosition in newPositions:
                if newPosition not in tmpPath:
                    movement.append(newPosition)

    return None


boardgame = Boardgame((5, 5))
boardgame.addOne((2, 2))
boardgame.addOne((4, 4))
boardgame.addOne((3, 1))


def testBFS(boardgame):
    size = boardgame.boardSize()
    print(BFS(boardgame, (0, 0), size))
    boardgame.addOne((1, 1))
    print(BFS(boardgame, (0, 0), size))


testBFS(boardgame)
