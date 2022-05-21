#include <iostream>
using namespace std;

class Solution{
  public:
  bool Compute(int &num){
    // cout << "num " << num << endl;
    int number = num;
    int reverseNum = 0, remainder = 0;
    
    while(number != 0){
        remainder = number % 10;
        reverseNum = reverseNum*10 + remainder;
        number = number / 10;
    }
    
    // cout << "number " << num << endl;
    // cout << "reverse " << reverseNum << endl;
    
    if(num == reverseNum){
        return true;
    }else{
        return false;
    }
      
  }
};


int main() {
	Solution s;
	
	int num = 1;
	cout << s.Compute(num) << endl;
	return 0;
}
