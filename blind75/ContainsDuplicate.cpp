#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    /*
    Returns true if there are no duplicates of any element in the vector.
    False if there exists a duplicate/copy.
    */
    bool containsDuplicate(vector<int>& nums) {
        // unordered map to hold occurences of the elements in nums
	unordered_map<int, int> umap;
        
	// iterate through the vector and increment the value(occurrence) of the key(which is the number in the vector)
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
	Solution s;
	vector<int> nums = {1,2,3,4};
	cout << s.containsDuplicate(nums);
	return 0;
}
