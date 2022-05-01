/*
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
*/

#include <iostream>
#include <string>

class Solution{
public:
   
    std::string compute(std::string s){
        std::string answer = "";
        int backspace = 0;
        int i = s.length() - 1;
        
        while(i > 0){
            if(s[i] == '#'){
                backspace++;
            }else{
                if(backspace == 0){
                    answer += s[i];
                }
                if(backspace > 0){
                    backspace--;
                }
            }
            i--;
        }
        return answer;
    }
    
    
    bool result(std::string s1, std::string s2){
        s1 = compute(s1);
        s2 = compute(s2);
        
        if(s1 == s2){
          return true;
        }
        return false;
    }  
};

int main() {
	Solution sobj;
	std::cout << sobj.result("ab##", "c#d#");
	
	// test with: Input: s = "ab#c", t = "ad#c", Input: s = "a#c", t = "b" 
	
	return 0;
}
