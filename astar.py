import heapq


class Node:
    def __init__(self, name, g_cost, h_cost, parent=None):
        self.name = name
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost


def a_star_search(graph, costs, start, goal, heuristic_values):

    open_list = []
    closed_list = set()

    # stores best cost to reach each node
    g_score = {start: 0}

    start_node = Node(start, 0, heuristic_values[start])
    heapq.heappush(open_list, start_node)

    while open_list:

        current_node = heapq.heappop(open_list)

        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        if current_node.name in closed_list:
            continue

        closed_list.add(current_node.name)

        for neighbor in graph.get(current_node.name, []):

            cost = costs[(current_node.name, neighbor)]
            tentative_g = current_node.g_cost + cost

            # Only update if better path found
            if neighbor not in g_score or tentative_g < g_score[neighbor]:

                g_score[neighbor] = tentative_g

                new_node = Node(
                    neighbor,
                    tentative_g,
                    heuristic_values[neighbor],
                    current_node
                )

                heapq.heappush(open_list, new_node)

    return None


def get_input():
    graph = {}
    heuristic_values = {}
    costs = {}

    print("Enter the graph structure:")
    n = int(input("Enter the number of nodes: "))

    for _ in range(n):
        node = input("Enter node name: ")
        neighbors = input(
            f"Enter neighbors for {node} (comma separated): "
        ).strip()

        if neighbors:
            graph[node] = [x.strip() for x in neighbors.split(",")]
        else:
            graph[node] = []

    print("\nEnter costs between nodes:")
    for node in graph:
        for neighbor in graph[node]:
            cost = int(input(f"Enter cost from {node} to {neighbor}: "))
            costs[(node, neighbor)] = cost

    print("\nEnter heuristic values:")
    for _ in range(n):
        node = input("Enter node name for heuristic: ")
        heuristic = int(input(f"Enter heuristic value for {node}: "))
        heuristic_values[node] = heuristic

    start = input("\nEnter the start node: ")
    goal = input("Enter the goal node: ")

    return graph, costs, heuristic_values, start, goal


# ---- Driver ----
graph, costs, heuristic_values, start, goal = get_input()
path = a_star_search(graph, costs, start, goal, heuristic_values)

if path:
    print(f"\nPath from {start} to {goal}: {path}")
else:
    print(f"\nNo path found from {start} to {goal}")

