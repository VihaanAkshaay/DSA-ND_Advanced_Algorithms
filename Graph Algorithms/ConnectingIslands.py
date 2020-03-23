# initialize an empty list
heap = list()

# insert 5 into heap
heapq.heappush(heap, 6)

# insert 6 into heap
heapq.heappush(heap, 6)

# insert 2 into heap
heapq.heappush(heap, 2)

# insert 1 into heap
heapq.heappush(heap, 1)

# insert 9 into heap
heapq.heappush(heap, 9)

print("After pushing, heap looks like: {}".format(heap))

# pop and return smallest element from the heap
smallest = heapq.heappop(heap)

print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(heap))

heap = list()

heapq.heappush(heap, (0, 1))

heapq.heappush(heap, (-1, 5))

heapq.heappush(heap, (2, 0))

heapq.heappush(heap, (5, -1))

print("After pushing, now heap looks like: {}".format(heap))

# pop and return smallest element from the heap
smallest = heapq.heappop(heap)

print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(heap))

import heapq


def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    """
    adjacency_list = [list() for _ in range(num_islands + 1)]

    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]
        adjacency_list[source].append((destination, cost))
        adjacency_list[destination].append((source, cost))

    return adjacency_list


def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """

    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1

    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]

    # initialize starting list - (edge_cost, neighbor)
    heap = [(0, start_vertex)]
    total_cost = 0

    while len(heap) > 0:
        cost, current_vertex = heapq.heappop(heap)

        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total-cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(heap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)