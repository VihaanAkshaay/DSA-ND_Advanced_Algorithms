class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


## Iterative Solution
def dfs_search(root_node, search_value):
    visited = []
    stack = [root_node]

    while len(stack) > 0:
        current_node = stack.pop()
        visited.append(current_node)

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited and child not in stack:
                stack.append(child)

## Recursive Solution
def dfs_recursion_start(self, start_node):
    visited = {}
    self.dfs_recursion(start_node, visited)


def dfs_recursion(self, node, visited):
    if (node == None):
        return False

    visited[node.value] = True
    print(node.value)

    for each in node.children:
        if (each.value not in visited):
            self.dfs_recursion(each, visited)