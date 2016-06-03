class Node:
    def __init__(self,data,left=None,right=None,parent=None):
        self.data = data
        self.right = right
        self.left = left
        self.parent = parent
    def __str__(self):
        return repr(self.data)

class BST:
    def __init__(self):
        self.root = None

    def search(self,i):
        if self.root:
            return self._search(self.root,i)
        else:
            return None
    def _search(self,x,i):
        if x.data == i:
            return x
        elif i < x.data:
            if x.left == None:
                return x
            else:
                return self._search(x.left,i)
        elif i > x.data:
            if x.right == None:
                return x
            else:
                return self._search(x.right,i)

    def insert(self,i):
        if not self.root:
            self.root = Node(i)
        else:
            x = self.search(i)
            y = Node(i,parent=x)
            if i < x.data:
                x.left = y
            else:
                x.right = y
    
    def delete(self,i):
        x = self.search(i)
        if x.data != i:
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
    bst.insert(i)

print(bst.search(5))
bst.delete(5)
print(bst.search(5))
