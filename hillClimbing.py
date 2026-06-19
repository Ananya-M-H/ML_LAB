import random

def objective_function(x):
  return -x ** 2 + 5

def hill_climbing(start_x, step_size, max_iterations):
  current_x = start_x
  current_score = objective_function(current_x)
  path = [(current_x, current_score)]  # store path

  for i in range(max_iterations):
        new_x = current_x + random.uniform(-step_size, step_size)
        new_score = objective_function(new_x)

        print(f"\nIteration {i + 1}")
        print(f"Current: x = {current_x:.4f}, f(x) = {current_score:.4f}")
        print(f"Candidate: x = {new_x:.4f}, f(x) = {new_score:.4f}")

        if new_score > current_score:
            print("Move: ACCEPTED ✅")
            current_x = new_x
            current_score = new_score
        else:
            print("Move: REJECTED ❌")

        path.append((current_x, current_score))  # track path

  print("\nFinal Solution:")
  print(f"x = {current_x:.4f}, f(x) = {current_score:.4f}")
  
  print("\nPath Taken:")
  for i, (x, score) in enumerate(path):
      print(f"Step {i}: x = {x:.4f}, f(x) = {score:.4f}")

  return current_x, current_score


best_x, best_score = hill_climbing(start_x=0.1, step_size=0.05, max_iterations=5)




def hill_climbing(graph, start, goal, heuristic):
    current = start
    path = [current]

    while current != goal:
        neighbors = graph[current]

        if not neighbors:
            print(f"No neighbors to explore from {current}. Stuck at local maxima.")
            return current, path

        print(f"\nCurrent node = {current}")
        print("Neighbors:")
        for n in neighbors:
            print(f"{n} ({heuristic[n]})")

        next_node = min(neighbors, key=lambda x: heuristic[x])

        print(f"Choose neighbor with minimum heuristic: {next_node} ({heuristic[next_node]})")

        if heuristic[next_node] >= heuristic[current]:
            print(f"Reached local maxima at {current}. Stopping search.")
            return current, path

        current = next_node
        path.append(current)

    return current, path


# Graph representation
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'E', 'D', 'F'],
    'D': ['A', 'F', 'C'],
    'E': ['B', 'C', 'H'],
    'F': ['G', 'C', 'D'],
    'G': [],
    'H': ['E', 'G']
}

heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10
}

start = 'A'
goal = 'G'

result, path = hill_climbing(graph, start, goal, heuristic)

print("\nPath:", " -> ".join(path))

if result == goal:
    print(f"Goal {goal} reached!")
else:
    print(f"Goal not reached. Stopped at {result}")