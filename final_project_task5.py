import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, traversal_colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if traversal_colors:
        colors = [traversal_colors[node[0]] for node in tree.nodes(data=True)]
    else:
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=3000, node_color=colors, font_size=16, font_color='white')
    plt.show()

def list_to_binary_heap(lst):
    def insert_node(index):
        if index < len(lst):
            node = Node(lst[index])
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            node.left = insert_node(left_index)
            node.right = insert_node(right_index)
            return node
        return None
    
    return insert_node(0)

def dfs(root):
    stack, visited = [root], []
    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return visited

def bfs(root):
    queue, visited = [root], []
    while queue:
        node = queue.pop(0)
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited

def generate_colors(n):
    colors = []
    for i in range(n):
        factor = i / (n - 1)
        r = int(18 + factor * (144 - 18))
        g = int(150 + factor * (240 - 150))
        b = int(240 + factor * (0 - 240))
        colors.append(f'#{r:02x}{g:02x}{b:02x}')
    return colors

def visualize_traversal(tree_root, traversal):
    nodes_in_order = traversal(tree_root)
    colors = generate_colors(len(nodes_in_order))
    traversal_colors = {node.id: colors[i] for i, node in enumerate(nodes_in_order)}
    draw_tree(tree_root, traversal_colors)

# Приклад використання
heap_list = [3, 1, 6, 5, 2, 4]
heap_root = list_to_binary_heap(heap_list)

# Візуалізація обходу в глибину (DFS)
print("DFS Order:", [node.val for node in dfs(heap_root)])
visualize_traversal(heap_root, dfs)

# Візуалізація обходу в ширину (BFS)
print("BFS Order:", [node.val for node in bfs(heap_root)])
visualize_traversal(heap_root, bfs)
