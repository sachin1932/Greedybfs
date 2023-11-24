#greedybfs
import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], start, 0, [start])]  # (heuristic, node, total cost, path)
    visited = set()

    while priority_queue:
        current_heuristic, current_node, total_cost, path = heapq.heappop(priority_queue)

        if current_node == goal:
            # Goal reached
            return True, path, total_cost

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, weight in graph[current_node].items():
                if neighbor not in visited:
                    neighbor_heuristic = heuristic[neighbor]
                    heapq.heappush(priority_queue, (neighbor_heuristic, neighbor, total_cost + weight, path + [neighbor]))

    # Goal not reachable
    return False, [], 0

# Example graph representation
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

# Heuristic function (straight-line distance to Bucharest)
heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Timisoara': 329,
    'Sibiu': 253,
    'Oradea': 380,
    'Lugoj': 244,
    'Fagaras': 178,
    'Rimnicu Vilcea': 193,
    'Mehadia': 241,
    'Dobreta': 242,
    'Craiova': 160,
    'Pitesti': 100,
    'Bucharest': 0
}

start_node = 'Arad'
goal_node = 'Bucharest'

result, path, total_cost = greedy_best_first_search(graph, start_node, goal_node, heuristic)

if result:
    print(f"Goal {goal_node} reached from {start_node} using Greedy Best-First Search.")
    print(f"Path followed: {path}")
    print(f"Total cost of the path: {total_cost}")
else:
    print(f"Goal {goal_node} not reachable from {start_node} using Greedy Best-First Search.")