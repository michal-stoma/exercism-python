class Node(object):
    def __init__(self, value, next_node=None):
        self.next_node = next_node
        self.node_value = value

    def value(self):
        return self.node_value

    def next(self):
        return self.next_node


class LinkedList(object):
    def __init__(self, values=[]):
        self.size = 0
        self.list_head = None

        for value in values:
            self.push(value)

    def __len__(self):
        return self.size

    def __iter__(self):
        _current_head = self.list_head
        while _current_head:
            yield _current_head.value()
            _current_head = _current_head.next()

    def head(self):
        if self.list_head is None:
            raise EmptyListException('List is empty.')

        return self.list_head

    def push(self, value):
        new_node = Node(value, self.list_head)
        self.size += 1
        self.list_head = new_node

    def pop(self):
        current_head = self.list_head
        self.list_head = self.head().next()
        self.size -= 1
        return current_head.value()

    def reversed(self):
        return LinkedList(self)


class EmptyListException(Exception):
    pass
