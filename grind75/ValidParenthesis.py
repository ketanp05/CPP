from collections import deque

class Solution:
	def isValid(self, s:str) -> bool:
		# parenthesis_map = {
		# 	"(":")",
		# 	"{":"}",
		# 	"[":"]"
		# }
		# stack = []


		# for letter in s:
		# 	if letter in parenthesis_map:
		# 		stack.append(parenthesis_map[letter])
		# 	elif stack and stack[-1] == letter: # stacks top element should be same as the current closing bracket
		# 		stack.pop()
		# 	else:
		# 		return False

		# for i in stack:
		# 	print(i)

		# if len(stack) > 0:
		# 	return False
		# return True

		parenthesis_map = {
			")":"(",
			"}":"{",
			"]":"["
		}
		stack = []

		for c in s:
			if c in parenthesis_map:
				if stack and stack[-1] == parenthesis_map[c]:
					stack.pop()
				else:
					return False
			else:
				stack.append(c)

		if not stack:
			return True

def main():
	solution_object = Solution()
	s = "({{{{}}}))"
	print(solution_object.isValid(s))

if __name__ == '__main__':
	main()