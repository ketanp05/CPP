from typing import List
from collections import defaultdict

class Solution:
	def groupAnagram(self, strs: List[str]) -> List[List[str]]:
		# groupAnagramResult = {}
		# for i in range(len(strs)):
		# 	for j in range(i+1, len(strs)):
		# 		if(strs[i] in groupAnagramResult.values()):
		# 			continue
		# 		if(sorted(strs[i]) == sorted(strs[j])):
		# 			groupAnagramResult[strs[i]] = strs[j]
		
		# for i in range(len(groupAnagramResult)):

		# defaultdict provides a default value for the key that does not exist
		# you can provide a default value, in this case its a list
		groupAnagramResult = defaultdict(list)

		
		for s in strs:
			count = [0] * 26
			for letter in s:
				# ord returns the ascii value of the letter
				count[ord(letter) - ord("a")] += 1

			# cause you cannot have key as a list, hence change it to tuple and tuples are non mutable
			groupAnagramResult[tuple(count)].append(s)

		# to avoid type error go with list(groupAnagramResult.values())
		return list(groupAnagramResult.values())

def main():
	strs = ["eat","tea","tan","ate","nat","bat"]
	print(Solution().groupAnagram(strs))

if __name__ == '__main__':
	main()