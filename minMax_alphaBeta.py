
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

def alphabeta(depth, node_index, is_maximizing_player, scores, target_depth, alpha, beta):
    if depth == target_depth:
        return scores[node_index]
   
    if is_maximizing_player:
        max_eval = float('-inf')
        for i in range(2):
            eval = alphabeta(depth + 1, node_index * 2 + i, False, scores, target_depth, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break 
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            eval = alphabeta(depth + 1, node_index * 2 + i, True, scores, target_depth, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval

print("Enter the depth of the game tree (e.g., 3 for 8 leaf nodes):")
tree_depth = int(input("Depth: "))
num_leaves = 2 ** tree_depth
print(f"Enter {num_leaves} leaf node scores separated by space:")
scores_input = input("Scores: ")
scores = list(map(int, scores_input.strip().split()))

if len(scores) != num_leaves:
    print(f"Error: Expected {num_leaves} scores, but got {len(scores)}.")
else:
    optimal_value = minimax(0, 0, True, scores, tree_depth)
    print(f"\nOptimal value using Minimax: {optimal_value}")
    optimal_value_ab = alphabeta(0, 0, True, scores, tree_depth, float('-inf'), float('inf'))
    print(f"Optimal value using Alpha-Beta Pruning: {optimal_value_ab}")
