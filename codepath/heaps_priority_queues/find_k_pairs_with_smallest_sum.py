import heapq
from typing import List

def k_smallest_pairs(nums1: List[int], nums2: List[int], k:int) -> List[List[int]]:
    # edge cases
    if k == 0 or not nums1 or not nums2:
        return []
    
    # initialize heap and result
    min_heap = []
    result = []

    # push pairs in heap for 1st of nums1 and all of nums2
    for j in range(min(k, len(nums2))):
        heapq.heappush(min_heap, (nums1[0]+nums2[j], 0, j))
    
    # extract min, push new pair if it exists
    while k > 0 and min_heap:
        sum_pair, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])

        # if i+1 element exists in nums1
        if i+1 < len(nums1):
            heapq.heappush(min_heap, (nums1[i+1]+nums2[j], i+1, j))
        
        k -= 1

    return result

def main():
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print(k_smallest_pairs(nums1, nums2, k)) 

if __name__ == "__main__":
    main()