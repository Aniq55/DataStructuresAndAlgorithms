class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self, data):
        node = LinkedListNode(data)
        self.head = node
        self.tail = node
        self.length = 1

    def add_node_at_the_end(self, data):
        node = LinkedListNode(data)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def add_node_at_the_beginning(self, data):
        node = LinkedListNode(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def add_node_at_position(self, position):
        pass

    def remove_node_from_the_beginning(self):
        pass

    def remove_node_from_the_end(self):
        pass

    def remove_node_from_position(self, position):
        pass