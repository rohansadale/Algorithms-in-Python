class Solution(object):
	def isPalindrome(self, x):
		if x < 0:
			return False

		div = 1
		while x/div >= 10:
			div *= 10
	
		while x > 0:
			left = x/div
			right = x%10

			if left != right:
				return False
			x = (x%div)/10
			div = div/100
		return True

s = Solution()
print s.isPalindrome(12321)
print s.isPalindrome(13321)
