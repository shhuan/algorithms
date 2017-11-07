/*
 *Given a string s and a dictionary of words dict, determine if s can be segmented into
 * a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

*/
#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <regex>
#include <unordered_set>


using namespace std;

class Solution {
public:
    bool wordBreak(string s, unordered_set<string>& wordDict) {

        vector<bool> f(s.length());
        fill(f.begin(), f.end(), false);

        for (int i=0; i<s.length(); i++){
            if (wordDict.find(s.substr(0,i+1)) != wordDict.end()){
                f[i] = true;
                continue;
            }
            for (int j = 0; j < i; ++j) {
                if (f[j] && wordDict.find(s.substr(j+1, i-j)) != wordDict.end()){
                    f[i] = true;
                    break;
                }
            }
        }
        return f[s.length()-1];
    }
};

int main(){
    Solution s;
    unordered_set<string> d{"leet", "code"};
    cout << s.wordBreak("leetcodes", d) << endl;
}