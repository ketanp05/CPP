#include <iostream>
#include <vector>

class Solution{
    
public:
    std::vector<int> compute(std::vector<int>& nums) {
    
        // int arrSize = sizeof(nums)/sizeof(int);
        
        int i = 0, j = 0, temp;

        while(i < nums.size()){
            if(nums[i] % 2 == 0){
                // temp = nums[i];
                // nums[i] = nums[j];
                // nums[j] = temp;
                std::swap(nums[i], nums[j]);
                j++;
            }

            i++;
        }

        // int k = 0;
        // while(k < arrSize){
        //     std::cout << nums[k] << " ";
        //     k++;
        // }
        
        return nums;
    }
};

int main() {
    Solution s;
    std::vector<int> nums{1,2,3,4,5,6,7,8,9,10};
    
    // int nums[] = {1,2,3,4,5,6,7,8,9,10};
    
	std::cout << s.compute(nums); // error here, please chek 
	
	return 0;
}
