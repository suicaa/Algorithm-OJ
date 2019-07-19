
# 请勿改动 Begin
class LinkedList:

  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    if self.next:
      return str(self.value) + " -> " + str(self.next)
    else:
      return str(self.value)
# 请勿改动 End

def make_linked_list(arr):
  dummy = LinkedList("dummy")
  tail = dummy
  for i in arr:
    tail.next = LinkedList(i)
    tail = tail.next
  return dummy.next

n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
print(make_linked_list(arr))
