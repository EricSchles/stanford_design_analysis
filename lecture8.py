class Node:
    def __init__(self,key,value,left=None,right=None,parent=None,color=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent
        self.color = color
    def __str__(self):
        return str(self.key)+":"+str(self.value)

class BST:
    def __init__(self):
        self.root = None

    def search(self,key):
        if self.root:
            return self._search(self.root,key)
        else:
            return None
    def _search(self,x,i):
        if x.key == i:
            return x
        elif i < x.key:
            if x.left == None:
                return x
            else:
                return self._search(x.left,i)
        elif i > x.key:
            if x.right == None:
                return x
            else:
                return self._search(x.right,i)

    def insert(self,key,value):
        if not self.root:
            self.root = Node(key,value,color="black")
        else:
            x = self.search(i)
            y = Node(key,value,parent=x)
            if i < x.key:
                x.left = y
            else:
                x.right = y
            y.color = "red"
            self.recolor(y)

    def recolor(self,x):
        if x is self.root: return
        p = x.parent
        if p.color == "black":
            return
        p_prime = p.parent
        if not p_prime:
            self.root.color = "black"
            return
        u = p_prime.right
        if u.color == "red":
            u.color,p.color = "black","black"
            p_prime.color = "red"
            self.recolor(p_prime)
        elif u.color == "black":
            p.color = "black"
            p_prime.color = "red"
            self.right_rotate(p_prime)

    def right_rotate(self,q_prime):
        #initialization
        if not q_prime.parent: return
        q = q_prime.parent
        l = q.left
        if not q.parent: return
        x = q.parent
        y = x.right

        #rotation
        q = x
        q.right = x
        x.parent = q
        q.left = l
        if l: l.parent = q
        x.left = q_prime
        q_prime.parent = x
        x.right = y
        if y: y.parent = x
        
    def delete(self,i):
        x = self.search(i)
        if x.key != i:
            return None
        if x.left == None:
            y = x.right
            y.parent = x.parent
            y.parent.right = y
            del x
        elif x.right == None:
            y = x.left
            y.parent = x.parent
            y.parent.right = y
            del x
        else:
            z = search(x.right,x.data)
            z_prime = z.right
            z.parent.left = z_prime
            z_prime.parent = z.parent
            x = z
            del x
            

bst = BST()
for i in range(10):
    bst.insert(i,i)

print(bst.search(5))
bst.delete(5)
print(bst.search(5))
