class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.value) + " -> " + str(self.next)
        else:
            return str(self.value)


def has_ring(a):
    j = a
    i = a
    while j.next != None:
        i = i.next
        j = j.next.next
        if i is j:
            return True
    return False
