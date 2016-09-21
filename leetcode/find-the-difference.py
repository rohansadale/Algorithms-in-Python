class Solution(object):
	def findTheDifference(self, s, t):
		result = 0
		for i in range(len(s)):
			result = result ^ ord(s[i])
		for i in range(len(t)):
			result = result ^ ord(t[i])
		return chr(result)

s = Solution()
print s.findTheDifference('abcd', 'abcde')
