/*
 * Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
 * Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ? b ? c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
*/

#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <chrono>

using namespace std;


class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if (nums.size() < 2){
            return vector<vector<int>>();
        }
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        set<string> exp;
        //Caution!!! nums.size() is unsigned integer, 0-2 will be very large
        for (int i = 0; i < nums.size()-2; ++i) {
            int v = nums[i];
            vector<vector<int>> s2 = move(twoSum(nums, 0-v, i+1, nums.size()-1));
            for (auto s : s2){
                s.push_back(v);
                sort(s.begin(), s.end());
                string k = hash(s);
//                exp.insert(k);
                if(exp.find(k) == exp.end()){
                    exp.insert(k);
                    res.push_back(s);
                }
            }
        }
//        for (string e : exp){
//            res.push_back(split(e, ','));
//        }
        return res;
    }

    string hash(vector<int>& nums){
        string res = "";
        for (int v : nums){
            if (res.length() > 0){
                res += ",";
            }
            ostringstream convert;   // stream used for the conversion
            convert << v;
            res += convert.str();
        }
        return res;
    }

    vector<int> split(string str, char delimiter) {
        vector<int> internal;
        stringstream ss(str); // Turn the string into a stream.
        string tok;
        while(getline(ss, tok, delimiter)) {
            internal.push_back(atoi(tok.c_str()));
        }
        return internal;
    }

    vector<vector<int>> twoSum(vector<int>& nums, int expect, int start, int end){
        vector<vector<int>> res;
        while (start < end){
            int s = nums[start] + nums[end];
            if (s == expect){
                res.push_back(vector<int>{nums[start], nums[end]});
                start++;
                end--;
            }else if(s < expect){
                start++;
            }else{
                end--;
            }
        }
        return res;
    }
};

void test(vector<int>& nums){
    Solution s;
    auto res = s.threeSum(nums);
    for (auto vc : res){
        for (int v : vc){
            cout << v << ", ";
        }
        cout << endl;
    }
    cout << endl;
}
int main(){
    vector<int> nums{-1, 0, 1, 2, -1, -4};
    test(nums);

    nums = vector<int>{1, 3, -4, -4};
    test(nums);

    nums.clear();
    test(nums);

    auto start = std::chrono::system_clock::now();
    nums = vector<int>{7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6};
    test(nums);

    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = end-start;
    cout << "Time Cost: " << elapsed_seconds.count() << endl;
}