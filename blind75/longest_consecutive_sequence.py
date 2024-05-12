from typing import List

class LongestCommonSequence:
    def longest_common_seq(self, nums: List[int]) -> int:
        """
        computes the longest sequence which is consecutive in the nums array

        Args:
        nums (List[int]): a list of integers

        Return:
        longest (int): length of the consecutive sequence
        """

        # naive brute force approach with O(nlogn) complexity
        # basically you use sorted(nums), sorting here leads to O(nlogn) complexity

        # to hold the length of our sequence
        longest = 0

        # convert the nums array into set for checking if n-1 and n+length exists in our nums
        # also having a set eliminates repititive comparisons
        nums_set = set(nums)

        for n in nums:
            # check if its a start of a sequence, basically n-1 should not exist in the set
            if (n-1) not in nums_set:
                # if you are here it means that n is the start of the seq
                # lets set this increment variable to check if consecutive sequence exist that follows n, basically n+1, (n+1)+1 and so on
                length = 0
                # we will keep checking if consecutive sequence exist but first the initial check will be if n exists or not in our set
                while (n+length) in nums_set:
                    length += 1
                # now you basically return the maximum of lenght/longest, cause longest might hold size of the current highest sequence, so we wanna return the max out of both
                longest = max(length, longest)
            
        return longest

def main():
    lcs = LongestCommonSequence()
    print(lcs.longest_common_seq([100,4,200,1,3,2]))
    print(lcs.longest_common_seq([0,3,7,2,5,8,4,6,0,1]))

if __name__ == "__main__":
    main()