#include <iostream>
using namespace std;

bool CheckPrime(int &num){
    //1
    // if(num == 0 or num == 1){
    //     return false;
    // }else if(num == 2){
    //     return true;
    // }else{
    //     int i = 2;
    //     while(i < num){
    //         if(num % i == 0){
    //             return false;
    //         }
    //         i++;
    //     }
    // }
    // return true;
    
    //2
    // if(num == 1){
    //     return false;
    // }
    // int i = 2;
    // while(i < num){
    //     if(num % i == 0){
    //         return false;
    //     }
    //     i++;
    // }
    // return true;
    
    //3
    if(num == 0 or num == 1){
        return false;
    }
    if(num == 2 || num == 3){
        return true;
    }
    if(num % 2 == 0 || num % 3 == 0){
        return false;
    }
    
    int i = 5;
    while(i*i <= num){
        if(num % i == 0 || num % (i+2) == 0){
            return false;
        }
        i=i+6;
    }
    return true;
    
}

int main() {
	// your code goes here
	int num = 29;
	cout << CheckPrime(num);
	
	
	return 0;
}
