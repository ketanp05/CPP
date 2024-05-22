from typing import List

class SearchRotatedArray:
    def search_in_rotated_array(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r)//2
            
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[l]:
                if (nums[l] <= target < nums[mid]):
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if (nums[mid] < target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

def main():
    sr = SearchRotatedArray()
    # input; [4,5,6,7,0,1,2]
    print(sr.search_in_rotated_array([1], 0))

if __name__ == "__main__":
    main()