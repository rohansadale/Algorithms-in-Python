class Stack:
    def __init__(self):
        self.items = []

    def size(self):
    	return len(self.items)

    def isempty(self):
    	return self.items == []

    def push(self, data):
    	self.items.append(data)

    def pop(self):
    	if not self.isempty():
    	  return self.items.pop()
    	print 'Stack is Empty. No element to pop!'

    def peek(self):
    	if not self.isempty():
    	  return self.items[-1]
    	print 'Stack is Empty. No element to peek!'

    def show(self):
    	for item in self.items:
    	  print item,
    	print


if __name__ == '__main__':
    s = Stack()
    print 'Is Empty ?' + str(s.isempty())
    s.push(10)
    s.push(20)
    s.push(30)
    s.show()
    print 'Pop - ' + str(s.pop())
    s.show()
    print 'Peek - ' + str(s.peek())
