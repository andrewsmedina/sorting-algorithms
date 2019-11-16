class Node:
    next = None
    value = None

class LinkedList:
    first_node = None
    def add(self, item):
        new_node = Node()
        new_node.value = item

        if not self.first_node:
            self.first_node = new_node
        else:
            node = self.first_node
            while node.next != None:
                node = node.next
            node.next = new_node

    def list(self):
        l = []
        node = self.first_node
        while node.next != None:
            l.append(node.value)
            node = node.next
        l.append(node.value)
        return l
