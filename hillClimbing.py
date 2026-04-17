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