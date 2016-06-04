import random

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

        
def depth_first_search(graph,start_node,current_time,level,capture):
    start_node.color = "grey"
    start_node.discovery_time = current_time
    current_time += 1
    try:
        capture[level].append(start_node.value)
    except:
        capture[level] = [start_node.value]
    for vertex in graph.internal[start_node]:
        if vertex.color == "white":
            vertex.parent = start_node
            current_time = depth_first_search(graph,vertex,current_time,level+1,capture)
            current_time += 1
    start_node.finish_time = current_time
    start_node.color = "black"
    return start_node.finish_time

def breathe_first_search(graph,start_node,current_time):
    start_node.color = "grey"
    

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
capture = {}
print("total time to end up back at start:",depth_first_search(g,start_node,0,0,capture))
print("nodes in graph:",[elem.value for elem in g.internal.keys()])
print("size of graph:",max([elem.value for elem in g.internal.keys()]))
print("start node:",start_node.value)
print("start node color:",start_node.color)
print("traversal path:")
for level in capture.keys():
    print(level,capture[level])
