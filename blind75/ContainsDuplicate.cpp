#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> umap;
        
        for(auto x : nums){
            umap[x]++;
            if(umap[x] > 1){
                return true;
            }
        }
        return false;
    }
};

int main() {
	// your code goes here
	Solution s;
	vector<int> nums = {1,2,3,4};
	cout << s.containsDuplicate(nums);
	return 0;
}
