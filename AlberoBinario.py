from Nodi import Node


class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = Node(key)

    def insert(self, key):
        if (self.root is None):
            self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        if (key <= currentNode.key):
            if (currentNode.left):
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = Node(key)
        elif (key > currentNode.key):
            if (currentNode.right):
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = Node(key)

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if (currentNode is None):
            return False
        elif (key == currentNode.key):
            return True
        elif (key < currentNode.key):
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)

    def inorder(self):
        def _inorder(v):
            if (v is None):
                return
            if (v.left is not None):
                _inorder(v.left)
            print(v.key)
            if (v.right is not None):
                _inorder(v.right)

        _inorder(self.root)

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def trapianto(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self.get(key, currentNode.left)
        else:
            return self.get(key, currentNode.right)

    def delete(self, key):
        z = self.get(key, self.root)
        if not (z.right or z.left):
            if z == z.p.left:
                z.p.left = None
            else:
                z.p.right = None
        elif z.left is None:
            self.trapianto(z, z.right)
        elif z.right is None:
            self.trapianto(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.p != z:
                self.trapianto(y, y.right)
                y.right = z.right
                y.right.p = y
            self.trapianto(z, y)
            y.left = z.left
            y.left.p = y
