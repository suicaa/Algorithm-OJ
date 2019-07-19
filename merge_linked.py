class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.value) + " -> " + str(self.next)
        else:
            return str(self.value)

def merge_linked_list(a, b):
    i = a
    j = b
    dummy = LinkedList("dummy")
    tail = dummy
    while i is not None or j is not None:
        if i is None:
            tail.next = j
            tail = j
            j = j.next
        elif j is None:
            tail.next = i
            tail = i
            i = i.next
        else:
            if i.value < j.value:
                tail.next = i
                tail = i
                i = i.next
            else:
                tail.next = j
                tail = j
                j = j.next

    return dummy.next
