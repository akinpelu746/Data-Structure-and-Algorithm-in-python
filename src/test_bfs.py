from collections import defaultdict


# Function to build the graph
def build_graph():
    edges = [
        ["A", "B"], ["B", "C"],
    ]
    graph = defaultdict(list)

    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]

        # Creating the graph
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph


# Python implementation to find the
# shortest path in the graph using
# dictionaries

# Function to find the shortest
# path between two nodes of a graph
def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", new_path)
                    return
                if neighbour in graph[goal]:
                    new_path.append(goal)
                    print("Shortest path = ", new_path)
                    return
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting" \
          "path doesn't exist :(")
    return


# Driver Code
if __name__ == "__main__":
    # Graph using dictionaries
    graph = {1: [3, 5], 2: [7], 3: [], 4: [], 5: [8, 4, 2], 6: [2], 7: [], 8: []}

    # Function Call
    BFS_SP(graph, 1, 6)
