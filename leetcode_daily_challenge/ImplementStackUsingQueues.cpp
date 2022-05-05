/*
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 
Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
*/

#include <iostream>
#include <queue>

class Solution{
public:
    std::queue<int> q1;
    std::queue<int> q2;
    
    void push(int x){
        q2.push(x);
        while(!q1.empty()){
            q2.push(q1.front());
            q1.pop();
        }
        
        std::swap(q1, q2);
    }
    
    int top(){
        return q1.front();
    }
    
    int pop(){
        int result = top();
        q1.pop();
        return result;
    }
    
    bool empty(){
        return q1.empty();
    }
};

int main() {
	// your code goes here
	Solution myStack;
    myStack.push(1);
    myStack.push(2);
    std::cout << myStack.top() << std::endl; // return 2
    std::cout << myStack.pop() << std::endl; // return 2
    myStack.empty(); // return False
	
	return 0;
}
