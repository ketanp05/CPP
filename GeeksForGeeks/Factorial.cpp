#include <iostream>
using namespace std;


class Solution{
  public:
    // check why const int &n (https://stackoverflow.com/questions/54032945/error-cannot-bind-non-const-lvalue-reference-of-type-int-to-an-rvalue-of-typ)
    int FactorialOfN(const int &n){
        if(n == 0 || n == 1){
            return 1;
        }
        return n * FactorialOfN(n-1);
    }
};

int main() {
	Solution s;
	
	int n = 5;
    cout << s.FactorialOfN(n) << endl;
	return 0;
}
