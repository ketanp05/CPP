from typing import List
from collections import Counter

class TopKFrequentElements:
    """
    a class to solve the top k frequent elements problem
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        keep a frequency count of numbers and return a list of ones that appear frequently

        Args:
        nums (List[int]): a list of integers
        k (int) : an integer

        Returns:
        List[int]: a list of 'k' integers returning the count of the k most frequently appearing elements
        """

        """
        first approach:
        1. does not account for:
            a. unique list: ideally should return an empty list for any k but it does not

        CODE
        

        # setting the keys as the number in nums and value as 0 initially
        for i in set(nums):
            hashmap[i] = 0

        # count the frequency of each number and record it in the hashmap
        for j in nums:
            hashmap[j] += 1

        return list(hashmap.keys())[:k]
        """

        """
        version 2
        1. Still does not account of unique nums case
        2. uses key for sorted inbuilt method as: lambda x:x[1]

        CODE
        # hashmap to keep the counter/frequency for each number in nums
        hashmap = {}

        # check if key exists if not update add the key and initialize the counter to 1
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        return [item for item, _ in sorted(hashmap.items(), key = lambda x: x[1], reverse=True)[:k]]
        """

        """
        version 3
        1. incorrect, does not account for 1 of the cases
            a. case: [1,2,2,3,3,4,3,3,4], 3

        CODE
        if k == 0 or not nums:
            return []

        # a counter hashmap for our nums input list with the help of the inbuild method Counter
        count_hashmap = Counter(nums)
        print(count_hashmap)

        # note: wait, Counter actually has a method called 'most_common(k)' which can be used to return a list of tuples(element, count) sorted from most frequent to the least
        return list(count_hashmap.keys())[:k]
        """

        """
        version 4:
        note: for now we do not care for the unique nums list being unique
        1. the below code solved most of the required edge cases
        2. tc: O(nlogn)
        
        CODE
        if k == 0 or not nums:
            return []
        
        element_count_hashmap = Counter(nums)

        return [item for item, _ in sorted(element_count_hashmap.items(), reverse=True)[:k]]
        """

        """
        1. Here is your todo:
        b. continue watching neetcode's approach
        
        if k == 0 or not nums:
            return []

        if len(nums) == 1:
            return nums

        # a counter hashmap for our nums input list with the help of the inbuild method Counter
        # count_hashmap = Counter(nums)
        count_hashmap = {}
        freq_count = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count_hashmap[n] = 1 + count_hashmap.get(n, 0)
        for num, cnt in count_hashmap.items():
            freq_count[cnt].append(num)

        result = []
        for j in range(len(nums) - 1, 0, -1):
            for ele in freq_count[j]:
                result.append(ele)
                if len(result) == k:
                    return result
        """
        if k == 0 or not nums:
            return []

        # Utilizing Counter to simplify frequency counting
        count_hashmap = Counter(nums)
        
        # Initialize the frequency count array with an extra space for the max frequency case
        freq_count = [[] for _ in range(len(nums) + 1)]
        
        for num, cnt in count_hashmap.items():
            freq_count[cnt].append(num)
        
        result = []
        # Iterate from the highest possible frequency down to 1
        for j in range(len(freq_count)-1, 0, -1):
            for ele in freq_count[j]:
                result.append(ele)
                if len(result) == k:
                    return result

def main():
    s = TopKFrequentElements()
    print(s.topKFrequent([1,1,1,2,3], 2))
    print(s.topKFrequent([], 2))
    print(s.topKFrequent([1,2,2,3,3,4,3,3,4], 3))
    print(s.topKFrequent([1], 1))
    print(s.topKFrequent([1,2,3,4,45,57,68], 2))

if __name__ == "__main__":
    main()