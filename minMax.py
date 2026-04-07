def minimax(depth, node_index, is_maximizing_player, scores, target_depth):
    if depth == target_depth:
        return scores[node_index]

    if is_maximizing_player:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, target_depth),
            minimax(depth + 1, node_index * 2 + 1, False, scores, target_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, target_depth),
            minimax(depth + 1, node_index * 2 + 1, True, scores, target_depth)
        )

print("Enter the depth of the game tree (e.g., 3 for 8 leaf nodes):")
tree_depth = int(input("Depth: "))
num_leaves = 2 ** tree_depth

print(f"Enter {num_leaves} leaf node scores separated by space:")
scores_input = input("Scores: ")
scores = [int(score) for score in scores_input.split()]

if len(scores) != num_leaves:
    print(f"Error: Expected {num_leaves} scores, but got {len(scores)}")
else:
    optimal_value = minimax(0, 0, True, scores, tree_depth)
    print(f"Optimal value using Minimax: {optimal_value}")
