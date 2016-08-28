# Queue using array(list)
class Queue1:
	def __init__(self):
		self.items = []

	def enqueue(self, data):
		self.items.insert(0, data)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def is_empty(self):
		return self.items == []

	def show(self):
		n = self.size()
		for i in range(n-1, -1, -1):
			print self.items[i],
		print

# Queue using linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue2:
	def __init__(self):
		self.front = None
		self.rear = None

	def enqueue(self, data):
		node = Node(data)
		if not self.front:
			self.front = node
			self.rear = node
		else:
			self.rear.next = node
			self.rear = node

	def dequeue(self):
		if self.front:
			node = self.front
			self.front = self.front.next
			return node.data

	def is_empty(self):
		return self.front == None

	def size(self):
		count = 0
		if self.front:
			temp = self.front
			while temp:
				count += 1
				temp = temp.next
		return count

	def show(self):
		temp = self.front
		while temp:
			print temp.data,
			temp = temp.next
		print

if __name__ == '__main__':
	print 'Queue using Array'
	q1 = Queue1()
	q1.enqueue(10)
	q1.enqueue(20)
	q1.enqueue(1)
	q1.show()
	q1.dequeue()
	print q1.size()
	q1.show()
	print 

	print 'Queue using Linked List'
	q2 = Queue2()
	q2.enqueue(10)
	q2.enqueue(20)
	q2.enqueue(1)
	q2.show()
	q2.dequeue()
	print q2.size()
	q2.show()