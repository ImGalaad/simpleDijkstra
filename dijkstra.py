def dijkstra_path(graph, start, end):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    unvisited = set(graph)
    previous = {}

    current = start
    while current != end:
        for neighbor in graph[current]:
            if neighbor in unvisited:
                new_distance = distances[current] + graph[current][neighbor]["weight"]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
        unvisited.remove(current)
        if not unvisited:
            return None
        candidates = {node: distances[node] for node in unvisited}
        current = min(candidates, key=candidates.get)

    path = []
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)

    return path[::-1]