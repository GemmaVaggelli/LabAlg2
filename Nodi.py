class Node:
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.red = False

    def get(self):
        return self.key

    def set(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if (self.left != None):
            children.append(self.left)
        if (self.right != None):
            children.append(self.right)
        return children
