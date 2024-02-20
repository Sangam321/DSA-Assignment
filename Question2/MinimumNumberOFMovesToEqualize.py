from collections import defaultdict, deque

def get_impacted_devices(edges, target_device):
    graph = defaultdict(list)
    visited = set()
    impacted_devices = []

    # Build the adjacency list representation of the network connections
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform BFS to find impacted devices
    queue = deque([target_device])
    visited.add(target_device)

    while queue:
        current_device = queue.popleft()

        # Traverse all connected devices
        for neighbor in graph[current_device]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                impacted_devices.append(neighbor)

    return sorted(impacted_devices)


edges = [[0,1],[0,2],[1,3],[1,6],[2,4],[4,6],[4,5],[5,7]]
target_device = 4
impacted_devices = get_impacted_devices(edges, target_device)
print("Impacted Device List:", impacted_devices)  # Output: [5, 7]
