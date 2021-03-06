class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push_node_value(self):
        pass

    def pop_node_value(self):
        pass

    def print_linked_list(self):
        current = self.head
        linked_list = []

        while current.next:
            linked_list.append(current.data)
            current = current.next
        linked_list.append(current.data)
        print linked_list

    def rev_linked_list(self):
        previous = self.head
        current = previous.next
        temp = current.next

        while current.next.next:
            current.next = previous
            previous = current
            current = temp
            temp = temp.next
        current.next = previous
        temp.next = current
        self.head.next = None
        self.head = temp

    def is_circular(self):
        pointer1 = self.head
        pointer2 = self.head.next

        # i = 0

        while pointer2.next.next:

            # print i
            # i += 1

            if pointer1 is pointer2:
                return True

            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

        return False

a = Node("s")
b = Node("t")
c = Node("e")
d = Node("p")
e = Node("h")
f = Node("a")
g = Node("n")
h = Node("i")
i = Node("e")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = a

stephanie = LinkedList()
stephanie.head = a

# stephanie.print_linked_list()
# stephanie.rev_linked_list()
# stephanie.print_linked_list()

print stephanie.is_circular()
