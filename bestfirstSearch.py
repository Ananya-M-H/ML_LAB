import heapq


class Node:
    def __init__(self, name, heuristic, parent=None):
        self.name = name
        self.heuristic = heuristic
        self.parent = parent

    # priority based on heuristic value
    def __lt__(self, other):
        return self.heuristic < other.heuristic


def best_first_search(graph, start, goal, heuristic_values):

    open_list = []      # priority queue
    open_set = set()    # quick lookup for duplicates
    closed_list = set()

    start_node = Node(start, heuristic_values[start])
    heapq.heappush(open_list, start_node)
    open_set.add(start)

    while open_list:

        current_node = heapq.heappop(open_list)
        open_set.discard(current_node.name)

        # Goal check
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        if current_node.name in closed_list:
            continue

        closed_list.add(current_node.name)

        # Expand neighbors
        for neighbor in graph.get(current_node.name, []):
            if (neighbor not in closed_list and
                    neighbor not in open_set):

                new_node = Node(
                    neighbor,
                    heuristic_values[neighbor],
                    current_node
                )

                heapq.heappush(open_list, new_node)
                open_set.add(neighbor)

    return None


def get_input():
    graph = {}
    heuristic_values = {}

    print("Enter the graph structure:")
    n = int(input("Enter the number of nodes: "))

    for _ in range(n):
        node = input("Enter node name: ")
        neighbors = input(
            f"Enter neighbors for {node} (comma separated): "
        ).strip()

        if neighbors:
            graph[node] = [n.strip() for n in neighbors.split(",")]
        else:
            graph[node] = []

    print("\nEnter heuristic values:")
    for _ in range(n):
        node = input("Enter node name for heuristic: ")
        heuristic = int(input(f"Enter heuristic value for {node}: "))
        heuristic_values[node] = heuristic

    start = input("\nEnter the start node: ")
    goal = input("Enter the goal node: ")

    return graph, heuristic_values, start, goal


# ---- Driver Code ----
graph, heuristic_values, start, goal = get_input()
path = best_first_search(graph, start, goal, heuristic_values)

if path:
    print(f"\nPath from {start} to {goal}: {path}")
else:
    print(f"\nNo path found from {start} to {goal}")
