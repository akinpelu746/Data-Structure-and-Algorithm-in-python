class Graph:
    def __init__(self, a, b):
        self.graph = {}
        self.A = A
        self.B = B

        self.saved_all = {}

    def create_graph(self, nodes):
        for i in range(1, n + 1):
            self.graph[i] = []

        for i in nodes:
            self.graph[i[0]] = self.graph[i[0]] + [i[1]]
            if i[0] not in self.graph[i[1]]:
                self.graph[i[1]] = self.graph[i[1]] + [i[0]]

    # Function to find the shortest
    # path between two nodes of a graph
    def BFS_SP(self, A, start, goal):
        explored = []

        # Queue for traversing the
        # graph in the BFS
        queue = [[start]]

        # If the desired node is
        # reached
        if start == goal:
            return

        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]

            # Condition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = self.graph[node]

                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    if neighbour not in explored:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)

                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour == goal:
                        self.saved_all[(start, goal)] = new_path
                        if A == 0:
                            self.saved_a[(start, goal)] = new_path
                        else:
                            self.saved_b[(start, goal)] = new_path
                        return
                explored.append(node)

        # Condition when the nodes
        # are not connected

        return

    def save_path(self):
        self.saved_a = {}
        self.saved_b = {}
        a_path = [[x, y] for path, x in enumerate(self.A) for y in self.A[path + 1:]]
        b_path = [[x, y] for path, x in enumerate(self.B) for y in self.B[path + 1:]]
        for i in a_path:
            if (i[0], i[1]) in self.saved_a:
                return
            elif (i[0], i[1]) in self.saved_all:
                self.saved_a[(i[0], i[1])] = self.saved_all[(i[0], i[1])]
                return
            self.BFS_SP(0, i[0], i[1])

        for j in b_path:
            if (j[0], j[1]) in self.saved_b:
                return
            elif (j[0], j[1]) in self.saved_all:
                self.saved_b[(j[0], j[1])] = self.saved_all[(j[0], j[1])]
                return
            self.BFS_SP(1, j[0], j[1])

    def swap_owner(self, x):
        if x in self.A:
            self.A.remove(x)
            self.B.append(x)
        else:
            self.B.remove(x)
            self.A.append(x)

    def compare(self, a, b):
        a_ave = []
        b_ave = []

        for keys, value in self.saved_a.items():
            if a in value and b in value:
                average_val = len(value)
                a_ave.append(average_val)

        for keys, value in self.saved_b.items():
            if a in value and b in value:
                average_val = len(value)
                b_ave.append(average_val)
        if len(a_ave) == 0 and len(b_ave) == 0:
            print('Tie')
        elif len(a_ave) == 0:
            print('B')
        elif len(b_ave) == 0:
            print('A')
        elif sum(a_ave) / len(a_ave) == sum(b_ave) / len(b_ave):
            print('Tie')
        elif sum(a_ave) / len(a_ave) > sum(b_ave) / len(b_ave):
            print('A')
        else:
            print('B')


n = 8
A = [2, 3, 4, 5, 7, 8]
B = [1, 6]
nodes = [[1, 3], [5, 8], [6, 2], [1, 5], [5, 4], [2, 7], [5, 2]]
graph = Graph(A, B)
graph.create_graph(nodes)
graph.save_path()
graph.compare(2, 6)
graph.compare(8, 7)
graph.swap_owner(8)
graph.swap_owner(1)
graph.save_path()
graph.compare(8, 7)
graph.compare(2, 5)
