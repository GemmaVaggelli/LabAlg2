from Nodi import Node
from AlberoBinario import ABR


class ARN(ABR):

    def __init__(self):
        super().__init__()
        self.nil = Node(None)

    def setRoot(self, key):
        self.root = Node(key)
        self.root.red = False
        self.root.p = self.nil
        self.root.left = self.nil
        self.root.right = self.nil

    def insert(self, key):
        if self.root is None:
            self.setRoot(key)
        else:
            self.insertRN(key)

    def insertRN(self, key):
        z = Node(key)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.red = True
        self.insertFixup(z)

    def insertFixup(self, z):
        while z.p.red:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.red:
                    z.p.red = False
                    y.red = False
                    z.p.p.red = True
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.red = False
                    z.p.p.red = True
                    self.right_rotate(z.p.p)
            else:
                if z.p == z.p.p.right:
                    y = z.p.p.left
                    if y.red:
                        z.p.red = False
                        y.red = False
                        z.p.p.red = True
                        z = z.p.p
                    else:
                        if z == z.p.left:
                            z = z.p
                            self.right_rotate(z)
                        z.p.red = False
                        z.p.p.red = True
                        self.left_rotate(z.p.p)
        self.root.red = False

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def inorderRN(self, x):
        if x is not self.nil:
            self.inorderRN(x.left)
            print(x.key)
            self.inorderRN(x.right)

    def findNode(self, currentNode, key):
        if currentNode is self.nil:
            return False
        elif key == currentNode.key:
            return True
        elif key < currentNode.key:
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)

    def minimum(self, x):
        while x.left is not self.nil:
            x = x.left
        return x