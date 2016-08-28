def check_parantheses(s):
	stack = []
	balanced_flag = True
	for ch in s:
		if ch in '([{':
			stack.append(ch)
		elif ch in ')}]' and len(stack) > 0:			
			ch_pop = stack.pop()
			if ch == ')':
				if ch_pop != '(': 
					balanced_flag = False
					break
			elif ch == '}':
				if ch_pop != '{': 
					balanced_flag = False
					break
			elif ch == ']':
				if ch_pop != '[': 
					balanced_flag = False
					break
		else:
			balanced_flag = False
			break
	if balanced_flag:
		print s + ' is Balanced'
	else:
		print s + ' is Unbalanced'

if __name__ == '__main__':
	s = '(()()()())'
	check_parantheses(s)

	s = '(((())))'
	check_parantheses(s)

	s = '()))'
	check_parantheses(s)

	s = '{{([][])}()}'
	check_parantheses(s)

	s = '[{}])'
	check_parantheses(s)