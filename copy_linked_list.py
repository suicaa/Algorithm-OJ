class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.value) + " -> " + str(self.next)
        else:
            return str(self.value)


def copy_linked_list(a):
    head = LinkedList("head")
    tail = head
    cur = a
    while cur:
        tail.next = LinkedList(cur.value)
        tail = tail.next
        cur = cur.next
    return head.next
