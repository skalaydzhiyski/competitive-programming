# Reverse a linked list
class Node:
	def __init__(self, value, next=None):
		self.value = value
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
current = head

inorder = ''
while current is not None:
	inorder += f'{current.value} -> '
	current = current.next
print(inorder)

rev = solve(head)

current = rev
revorder = ''
while current is not None:
	revorder += f'{current.value} -> '
	current = current.next
print(revorder)