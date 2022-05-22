// #include <iostream>

// using namespace std;

// class Solution{
//   public:
//     int HighestCommonFactor(int &a, int &b){
//         int hcf = min(a, b);
        
//         while(hcf > 0){
//             if(a % hcf == 0 && b % hcf == 0){
//                 break;
//             }
//             hcf--;
//         }
//         return hcf;
//     }
    
// };

// int main(){
// 	Solution s;
	
// 	int a = 13, b = 3;
//     cout << s.HighestCommonFactor(a,b) << endl;
// 	return 0;
// }




#include <iostream>
using namespace std;

// class Solution{
//     public:
//     int HighestCommonFactorOrGreatestCommonDivisor(int &a, int &b){
//         // euclidean algorithm
//         while(a != b){
//             if(a > b){
//                 a = a - b;
//             }else{
//                 b = b - a;
//             }
            
//             // since a and b will evntually be common
//             return a;
//         }
//     }
// };

// int main() {
// 	Solution s;
// 	int a = 5, b = 10;
// 	cout << s.HighestCommonFactorOrGreatestCommonDivisor(a, b) << endl;
// 	return 0;
// }



// #include <iostream>
// using namespace std;

// class Solution{
//     public:
//     int HighestCommonFactorOrGreatestCommonDivisor(int a, int b){
//         // euclidean algorithm
//         if(b == 0){
//             return a;
//         }
//         return HighestCommonFactorOrGreatestCommonDivisor(b, a % b);
//     }
// };

// int main() {
// 	Solution s;
// 	int a = 5, b = 10;
// 	cout << s.HighestCommonFactorOrGreatestCommonDivisor(a, b) << endl;
// 	return 0;
// }



