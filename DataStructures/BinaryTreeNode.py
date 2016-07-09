class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self, data):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def insert_left(self, newNode):
        if self.left is None:
            self.left = BinaryTreeNode(newNode)
        else:
            temp = BinaryTreeNode(newNode)
            temp.left = self.left
            self.left = temp

    def insert_right(self, newNode):
        if self.right is None:
            self.right = BinaryTreeNode(newNode)
        else:
            temp = BinaryTreeNode(newNode)
            temp.right = self.right
            self.right = temp


def insert_into_binary_tree_using_level_order(root, data):
    import Queue
    newNode = BinaryTreeNode(data)
    if root is None:
        root = newNode
        return root

    q = Queue()
    q.enQueue(root)


