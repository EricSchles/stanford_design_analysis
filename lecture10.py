import random

class TreeNode:
    def __init__(self,value,color="white",parent=None,children=[],discovery_time=None,finish_time=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.children = children
        self.discovery_time = discovery_time
        self.finish_time = finish_time
    def __str__(self):
        return repr(self.value)

class GraphNode:
    def __init__(self,value,color="white",parent=None,discovery_time=None,finish_time=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.discovery_time = discovery_time
        self.finish_time = finish_time
    def __str__(self):
        return repr(self.value)
 
class Graph:
    def __init__(self):
        self.internal = {}

    def add_node(self,value):
        self.internal[value] = []

    def add_connection(self,from_node,to_node):
        self.internal[from_node].append(to_node)

        
def depth_first_search(graph,tree,start_node,current_time):
    cur = TreeNode(start_node)
    cur.parent = tree
    start_node.color = "grey"
    start_node.discovery_time = current_time
    current_time += 1
    for vertex in graph.internal[start_node]:
        cur.children.append(TreeNode(vertex))
        if vertex.color == "white":
            vertex.parent = start_node
            current_time = depth_first_search(graph,cur,vertex,current_time)
            current_time += 1
    start_node.finish_time = current_time
    start_node.color = "black"
    return start_node.finish_time

def print_tree(cur_node,seen_nodes):
    if cur_node:
        print(cur_node.value)
        seen_nodes.append(cur_node)
        print()
        for elem in cur_node.children:
            if elem in seen_nodes: continue
            print_tree(elem,seen_nodes)

g = Graph()
graph_nodes = []
for i in range(20):
    node = GraphNode(i)
    g.add_node(node)
    if i != 0:
        g.add_connection(node,graph_nodes[random.randint(0,len(graph_nodes)-1)])
    for g_node in graph_nodes:
        if random.choice([1,2,3]) == 1:
            g.add_connection(node,g_node)
    graph_nodes.append(node)


start_node = graph_nodes[random.randint(0,len(graph_nodes)-1)]
root = TreeNode(None)
root.children.append(TreeNode(start_node))
print(depth_first_search(g,root,start_node,0))
print_tree(root,[])
    
