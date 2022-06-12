from typing import List
from collections import defaultdict

class Solution:
	def topKFrequent(self, nums:List[int], k:int) -> List[int]:
		# frequency = dict()
		# for num in nums:
		# 	frequency[num] = 1 + frequency.get(num, 0)

		# i = -1
		# temp = list()
		# for itr in range(k):
		# 	temp.append(sorted(frequency.values())[i])
		# 	i -= 1

		# high_frequency_values = list()
		# for key, value in frequency.items():
		# 	if value in temp:
		# 		high_frequency_values.append(key)

		# return high_frequency_values

		# result = zip(frequency.keys(), frequency.values())
		# return list(result)

		count = {}
		frequency = [[] for i in range(len(nums)+1)]

		for n in nums:
			count[n] = 1 + count.get(n, 0)

		for key, value in count.items():
			frequency[value].append(key)

		result = []
		for i in range(len(frequency)-1, 0, -1):
			for n in frequency[i]:
				result.append(n)
				if len(result) == k:
					return result


def main():
	s = Solution()
	nums = [1,1,1,1,2,2,3]
	# nums = [1]
	k = 2;
	print(s.topKFrequent(nums, k))

if __name__ == "__main__":
	main()