// #include <iostream>
// using namespace std;


// class Solution{
//   public:
//     // check why const int &n (https://stackoverflow.com/questions/54032945/error-cannot-bind-non-const-lvalue-reference-of-type-int-to-an-rvalue-of-typ)
//     int TrailingZeroInFactorial(int n){
//         // if(n == 0 || n == 1){
//         //     return 1;
//         // }
//         // int fact = n * FactorialOfN(n-1);
//         // cout << fact << endl;
        
//         int fact = 1;
//         while(n!=0){
//             fact = fact * n;
//             n--;
//         }
        
//         int trailingZeroCount = 0;
//         while(fact != 0){
//             if(fact % 10 == 0){
//                 trailingZeroCount += 1;
//             }
//             fact = fact / 10;
//         }
//         return trailingZeroCount;
//     }
    
// };

// int main() {
// 	Solution s;
	
// 	int n = 10;
//     cout << s.TrailingZeroInFactorial(n) << endl;
// 	return 0;
// }

#include <iostream>
using namespace std;

class Solution{
  public:
    int TrailingZeroInFactorial(int n){
        int count = 0;
        for(int i = 5; i <= n; i=i*5){
            count += n/i;
        }
        return count;
    }
};

int main(){
	Solution s;

	int n = 251;
	cout << s.TrailingZeroInFactorial(n) << endl;
	return 0;
}
