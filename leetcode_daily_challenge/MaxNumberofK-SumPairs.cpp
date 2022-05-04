/*
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
*/

#include <iostream>
#include <vector>
#include <algorithm>
// using namespace std;

class Solution{
public:
    int Compute(std::vector<int> v, int key){
        // return pairs whose sum equals key
        // int paircount = 0;
        
        // for(int i = 0; i < v.size() ; i++){
        //     for(int j = i + 1; j < v.size(); j++){
        //         if(v[i] + v[j] == key){
        //             std::cout << v[i] << v[j] << std::endl;
        //             paircount++;
        //             std::cout << "pair count: " << paircount << std::endl;
        //         }
        //     }
        // }
        
        // return paircount;
        
        std::sort(nums.begin(), nums.end());
        
        
        int i = 0; int j = nums.size() - 1;
        int count = 0; int sum = 0;
        
        while(i < j){
            sum = nums[i] + nums[j];
            if(sum == key){
                count++;
                i++;
                j--;
            }else if(sum > key){
                j--;
            }else{
                i++;
            }
        }
        
        return count;
    }
};

int main() {
	// your code goes here
	Solution s;
	
	std::vector<int> nums{3,1,3,4,3};
	int key = 6;
	
	std::cout << s.Compute(nums, key) << std::endl;
	
	return 0;
}
