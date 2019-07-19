class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.value) + " -> " + str(self.next)
        else:
            return str(self.value)


def insert_linked_list(a, v):
    head = LinkedList("head")
    head.next = a
    cur = head

    while cur.next is not None:
        if v < cur.next.value:
            newnode = LinkedList(v)
            newnode.next = cur.next
            cur.next = newnode
            return head.next
        cur = cur.next

    cur.next = LinkedList(v)
    return head.next
