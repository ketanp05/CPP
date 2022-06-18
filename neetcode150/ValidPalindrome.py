class Solution:
	def isPalindrome(self, s:str) -> bool:
		bad_chars = ['*',',',':',';']
		s = ''.join(filter(lambda i: i not in bad_chars and i != " ", s)).lower()
		if s == s[::-1]:
			return True
		return False


def main():
	obj = Solution()

	# s = "A man, a plan, a canal: Panama"
	s = "race a car"
	print(obj.isPalindrome(s))

if __name__ == '__main__':
	main()