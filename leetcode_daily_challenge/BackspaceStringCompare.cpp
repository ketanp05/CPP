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
	// your code goes here
	Solution sobj;
	std::cout << sobj.result("ab##", "c#d#");
	
	// test with: Input: s = "ab#c", t = "ad#c", Input: s = "a#c", t = "b" 
	
	return 0;
}
