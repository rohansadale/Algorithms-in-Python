prec = {}
prec['('] = 0
prec['+'] = 1
prec['-'] = 1
prec['*'] = 2
prec['/'] = 2

def infix_postfix(s):
	opstack = []
	postfix = []
	for token in s:
		if token == '(':
			opstack.append(token)
		elif token.isalnum():
			postfix.append(token)
		elif token == ')':
			top_token = opstack.pop()
			while top_token != '(':
				postfix.append(top_token)
				top_token = opstack.pop()
		else:
			while (len(opstack) != 0) and (prec[opstack[-1]] > prec[token]):
				postfix.append(opstack.pop())
			opstack.append(token)
	while len(opstack) != 0:
		postfix.append(opstack.pop())

	return ''.join(postfix)

def infix_prefix(s):
	operator_stack = []
	operand_stack = []
	prefix = []
	for token in s:
		if token.isalnum():
			operand_stack.append(token)
		elif token == '(':
			operator_stack.append(token)
		elif token == ')':
			while operator_stack[-1] != '(':
				op = operator_stack.pop()
				num1 = operand_stack.pop()
				num2 = operand_stack.pop()
				op = op + num1 + num2
				operand_stack.append(op)
			operator_stack.pop()
		elif len(operator_stack) == 0 or prec[token] > prec[operator_stack[-1]]:
			operator_stack.append(token)
		elif prec[token] < prec[operator_stack[-1]]:
			while len(operator_stack) > 0 and prec[token] < prec[operator_stack[-1]]:
				op = operator_stack.pop()
				num1 = operand_stack.pop()
				num2 = operand_stack.pop()
				op = op + num1 + num2
				operand_stack.append(op)
			operator_stack.append(token)

	while len(operator_stack) != 0:
		op = operator_stack.pop()
		num1 = operand_stack.pop()
		num2 = operand_stack.pop()
		op = op + num2 + num1
		operand_stack.append(op)

	return ''.join(operand_stack)


if __name__ == '__main__':
	s = 'A * B + C * D'
	print 'Infix - ' + s 
	print 'Postfix - ' + infix_postfix(s.split())
	print 'Prefix - ' + infix_prefix(s.split())
	print 
	s = '( A + B ) * C - ( D - E ) * ( F + G )'
	print 'Infix - ' + s 
	print 'Postfix - ' + infix_postfix(s.split())
	print 'Prefix - ' + infix_prefix(s.split())	

