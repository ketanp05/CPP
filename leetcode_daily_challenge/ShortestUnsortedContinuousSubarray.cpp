/*
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
*/

#include <iostream>
#include <vector>
// using namespace std;

class Solution {
public:
    int findUnsortedSubarray(std::vector<int>& nums) {
        int a = -1;
        int first = nums[0];
        
        
        // part 1
        for(int i = 1; i < nums.size(); i++){
            if(first > nums[i]){
                a = i;
                // std::cout << "a inside loop: " << a << std::endl;
            }else{
                first = nums[i];
                // std::cout << "first: " << first << std::endl;
            }
        }
        
        std::cout << "a:" << a << std::endl;
        
        
        // std::cout << std::endl;
        
        // part 2
        int b = 0;
        int last = nums[nums.size() - 1];
        
        for(int i = nums.size() - 2; i >= 0; i--){
            if(last < nums[i]){
                b = i;
                // std::cout << "b inside loop: " << b << std::endl;
            }else{
                last = nums[i];
                // std::cout << "last: " << last << std::endl;
            }
        }
        
        std::cout << "b:" << b << std::endl; 
            
        return a - b + 1;
    }
};

int main() {
	
	std::vector<int> nums{ 2,6,4,8,10,9,15 };
	Solution s;
	std::cout << s.findUnsortedSubarray(nums);
	
	return 0;
}
