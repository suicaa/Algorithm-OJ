class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.value) + " -> " + str(self.next)
        else:
            return str(self.value)


def middle_point(a):
    if a.next == None:
        return None
    slow = a
    fast = a
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow
