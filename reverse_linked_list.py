class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.value) + " -> " + str(self.next)
        else:
            return str(self.value)

def reverse_linked_list(a):
    if a is None or a.next is None:
        return a
    head = a
    cur = a.next
    while cur is not None:
        cur_new = cur.next
        a.next = cur_new
        cur.next = head
        head = cur
        cur = cur_new
    return head




