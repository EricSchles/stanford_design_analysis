import random

class Stack:
    def __init__(self):
        self.internal = []
    def push(self,data):
        self.internal.append(data)
    def pop(self):
        return self.internal.pop()
    def is_empty(self):
        return self.internal == []
    
class Queue:
    def __init__(self):
        self.internal = []
    def push(self,data):
        self.internal.insert(0,data)
    def pop(self):
        return self.internal.pop()
    def is_empty(self):
        return self.internal == []

def extended_bfs(start_node,graph,num_nodes):
    already_seen = []
    levels = [[] for _ in range(num_nodes)]
    levels[0] = [start_node]
    already_seen.append(start_node)
    for i in range(num_nodes):
        if levels[i] == []:
            break
        while levels[i] != []:
            u = levels[i].pop()
            for x in graph[i]:
                if not x in already_seen:
                    already_seen.append(x)
                    levels[i+1].append(x)
    return already_seen
    
def dfs(start_node,graph):
    stack = Stack()
    stack.push(start_node)
    print("traversal for dfs:")
    first_time = True
    already_seen = []
    while not stack.is_empty():
        next_node = stack.pop()
        if next_node == start_node and not first_time: return
        [stack.push(elem) for elem in graph[next_node] if not elem in already_seen]
        already_seen.append(next_node)
        print(next_node,end=" ")
        first_time = False
    print()

def bfs(start_node,graph):
    queue = Queue()
    queue.push(start_node)
    print("traversal for bfs:")
    first_time = True
    already_seen = []
    while not queue.is_empty():
        next_node = queue.pop()
        if next_node == start_node and not first_time: return
        [queue.push(elem) for elem in graph[next_node] if not elem in already_seen]
        already_seen.append(next_node)
        print(next_node,end=" ")
        first_time = False
    print()

def path(listing):
    for elem in listing:
        print(elem,end=" -> ")

def distance(path,a,b):
    index_a = path.index(a)
    index_b = path.index(b)
    if index_a < index_b:
        return index_b-index_a
    else:
        return index_b + (path.index(path[-1]) - index_a)
    
g = {}
for node in range(20):
    g[node] = [elem for elem in range(20)]
    g[node].remove(node)
    listing = g[node][:]
    [g[node].remove(i) for i in listing if random.choice([1,2,3]) == 1]

start_node = random.randint(0,19)
print("start_node:",start_node)
print("children:",g[start_node])
count = 0
for i in range(20):
    if start_node in g[i]:
        count += 1
print("percentage of nodes directly connected to start node:",count/20*100)
shortest_path = extended_bfs(start_node,g,20)
print(path(shortest_path))
print(distance(shortest_path,1,5))
#print()
#dfs(start_node,g)
