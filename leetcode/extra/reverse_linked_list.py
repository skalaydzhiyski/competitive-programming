# Reverse a linked list
class Node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def solve(head):
	current = head
	prev = None
	while current is not None:
		temp = current.next
		current.next = prev
		prev = current
		current = temp
	return prev

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
res = solve(head)
while res is not None:
	print(res.val)
	res = res.next