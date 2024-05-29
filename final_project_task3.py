import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Ініціалізація бінарної купи
    heap = [(0, start)]
    
    while heap:
        # Вибір вершини з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(heap)
        
        # Перевірка, чи поточна відстань коректна
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлення відстаней до сусідніх вершин
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances

# Приклад використання
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
start_vertex = 'A'
print(dijkstra(graph, start_vertex))
