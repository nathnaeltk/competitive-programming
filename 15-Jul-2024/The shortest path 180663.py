# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import deque, defaultdict

def find_shortest_path(src, dest):
    queue = deque([src])
    visited = {src: None}
    
    while queue:
        current = queue.popleft()
        
        if current == dest:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return len(path) - 1, path[::-1]
        
        for neighbor in adjacency_list[current]:
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
    
    return -1, []

if __name__ == "__main__":
    nodes, edges = map(int, input().split())
    source, target = map(int, input().split())

    adjacency_list = defaultdict(list)
    for _ in range(edges):
        node1, node2 = map(int, input().split())
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)
        
    distance, path = find_shortest_path(source, target)
    if distance == -1:
        print(-1)
    else:
        print(distance)
        print(*path)
