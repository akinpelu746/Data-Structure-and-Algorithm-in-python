class escape:

    def __init__(self, size, maze, s, e, ri, ci):
        self.allowedMove = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.maze = maze
        self.s = s
        self.e = e
        self.ri = ri
        self.ci = ci
        self.size = size

    def movements(self, currPosition):
        possible_pos = []
        for i in self.allowedMove:
            new_pos = currPosition[0] + i[0], currPosition[1] + i[1]
            "check if the new position is possible on the board"
            if self.size[0] >= new_pos[0] >= 0 and self.size[1] >= new_pos[1] >= 0:
                possible_pos.append((new_pos))
        return possible_pos

    def generate(self, ri, ci, securedArea=[]):
        while ri > 0:
            result = self.movements(ci)
            for i in result:
                if self.maze[i] == self.s or self.maze[i] == self.e:
                    return ("not possible")
                elif self.maze[i] != "#":
                    securedArea.append(i)
                    self.generate(ri - 1, i, securedArea)
        return securedArea

    def minimumsteps(self):
        guard_watch = self.generate(self.ri, self.ci)
        if guard_watch == "not possible":
            return "Impossible"
        path = [self.ci]
        savedMove = [path]
        while len(savedMove) > 0:
            tempMove = path.pop(0)
            currPos = savedMove[-1]
            if currPos == self.e:
                return len(savedMove)
            newPositions = self.movements(currPos)
            for newPosition in newPositions:
                " Avoid loops and guard reach "
                if newPosition not in tempMove and newPositions not in guard_watch and self.maze[newPositions] == "#":
                    newPath = tempMove + [newPosition]
                    savedMove.append(newPath)
        return "Impossible"


""" Todo 
1.Implement for mutiple guard
2.read and parse the file
3. Debug """
