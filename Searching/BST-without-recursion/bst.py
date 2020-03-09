#Binary Tree Algorithm

class BinaryTree():

    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    def insert(self, root, node):
        if self.root is None: 
            self.root = self.node

        else:
            if self.root.value < self.node.value:
                if self.root.right is None:
                    self.root.right = self.node
                else:
                    insert(self.root.right, self.node)
                else:
                    if self.root.left is None:
                        self.root.left = self.node
                    else:
                        insert(self.root.left, self.node)
    def inorder(self, root):
        if self.root:
            inorder(self.root.left)
            print(self.root.value)
            inorder(self.root.right)

