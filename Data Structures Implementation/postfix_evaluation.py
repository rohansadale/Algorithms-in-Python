def evaluate(s):
	opstack = []
	for token in s:
		if token in ['+', '-', '*', '/']:
			num1 = int(opstack.pop())
			num2 = int(opstack.pop())
			if token == '+':
				num = num1+num2
			elif token == '-':
				num = num1-num2
			elif token == '*':
				num = num1*num2
			elif token == '/':
				num = num2/num1
			opstack.append(num)
		else:
			opstack.append(token)	
	return opstack[0]

if __name__ == '__main__':
	s = '7 8 + 3 2 + /'
	print evaluate(s.split())