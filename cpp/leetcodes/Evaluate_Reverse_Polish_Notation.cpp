/*
 * Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
 */

#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        if (tokens.empty()){
            return 0;
        }
        stack<int> s;
        set<string> ops{"+","-","*","/"};
        for (string t : tokens){
            if (ops.find(t) != ops.end()){
                int rv = s.top();
                s.pop();
                int lv = s.top();
                s.pop();
                if (t == "+"){
                    s.push(lv + rv);
                }else if(t == "-"){
                    s.push(lv - rv);
                }else if(t == "*"){
                    s.push(lv * rv);
                }else{
                    s.push(lv / rv);
                }
            }else{
                s.push(atoi(t.c_str()));
            }
        }
        return s.top();
    }
};


int main(){
    Solution s;
    auto exp = vector<string>{"12","-5","/"};
    cout << s.evalRPN(exp) << endl;

    exp = vector<string>{"2"};
    cout << s.evalRPN(exp) << endl;

    exp = vector<string>{"-3", "9", "*"};
    cout << s.evalRPN(exp) << endl;
}