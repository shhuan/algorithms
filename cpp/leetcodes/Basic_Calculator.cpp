/*
 * Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.

 */


#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <regex>


using namespace std;


class Solution {
public:
    int calculate(string s) {
        return calRPN(toRPN(s));
    }
    vector<string> toRPN(string s){
        vector<string> v;
        vector<string> exp = toExp(s);
        vector<string> rpn;
        stack<string> sk;
        set<string> operators{"+", "-", "*", "/", "(", ")"};
        for (auto op : exp){
            if (operators.find(op) != operators.end()){
                if (op == "("){
                    sk.push(op);
                }else if(op == ")"){
                    while (sk.top() != "("){
                        rpn.push_back(sk.top());
                        sk.pop();
                    }
                    sk.pop();
                }else{
                    while (!sk.empty() && sk.top() != "("){
                        rpn.push_back(sk.top());
                        sk.pop();
                    }
                    sk.push(op);
                }
            }else{
                rpn.push_back(op);
            }
        }
        while (!sk.empty()) {
            rpn.push_back(sk.top());
            sk.pop();
        }
        return rpn;
    }
    int calRPN(vector<string> rpn){
        if (rpn.empty()){
            return 0;
        }
        stack<int> s;
        set<string> ops{"+","-","*","/"};
        for (string t : rpn){
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

    vector<string> toExp(string str){
        vector<string> exp;
        for (char ch : str){
            if (ch == '+' || ch == '-' || ch == '(' || ch == ')'){
                exp.push_back(string(1, ch));
            }else if (ch != ' '){
                if (exp.empty()){
                    exp.push_back(string(1, ch));
                }else{
                    string last = exp.back();
                    if (last[0] > '9' || last[0] < '0'){
                        exp.push_back(string(1, ch));
                    }else{
                        exp.pop_back();
                        exp.push_back(last+string(1,ch));
                    }
                }
            }
        }
        return exp;
    }
    vector<string> split(string str, char delimiter) {
        vector<string> internal;
        stringstream ss(str); // Turn the string into a stream.
        string tok;
        while(getline(ss, tok, delimiter)) {
            internal.push_back(tok);
        }
        return internal;
    }

};

int main(){
    Solution s;
    auto exp = s.toExp(" 1 +  1");
    for (auto e : exp){
        cout << e;
    }
    cout << endl;
    cout << s.calculate("1 + 1") << endl;
    cout << s.calculate(" 2-1 + 2 ") << endl;
    cout << s.calculate("(1+(4+5+2)-3)+(6+8)") << endl;

}