class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.value) + " -> " + str(self.next)
        else:
            return str(self.value)


def concat_linked_list(a, b):
    cur = a
    while cur.next != None:
        cur = cur.next
    cur.next = b

    return a


