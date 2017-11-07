#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>

using namespace std;

/*
 * Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.

 */
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.empty()){
            return 0;
        }
        auto iter = nums.begin();
        int pc = 0;
        int pv = *iter == 0 ? -1 : 0;
        for(int v : nums){
            if (v != pv){
                pc = 1;
                *iter = v;
                pv = v;
                iter++;
            }else{
                if (pc < 2){
                    pc += 1;
                    *iter = v;
                    pv = v;
                    iter++;
                }
            }
        }

        nums.erase(iter, nums.end());
        return nums.size();
    }
    int removeDuplicates2(vector<int>& nums){
        int i = 0;
        for (int n : nums)
            if (i < 2 || n > nums[i-2])
                nums[i++] = n;
        return i;
    }

    template <typename T>
    void outoutList(vector<T>& nums){
        for_each(begin(nums), end(nums), [](T& v){
           cout << v << " ";
        });
        cout << endl;
    }
};

int main(){
    Solution s;
    auto v = vector<int>{1, 1, 1, 2, 2, 3};
    cout << s.removeDuplicates(v) << endl;
    s.outoutList(v);

    v = vector<int>{2};
    cout << s.removeDuplicates(v) << endl;
    s.outoutList(v);

    v.clear();
    cout << s.removeDuplicates(v) << endl;
    s.outoutList(v);

    v = vector<int>{1, 2};
    cout << s.removeDuplicates(v) << endl;
    s.outoutList(v);

    v = vector<int>{1, 2, 2};
    cout << s.removeDuplicates(v) << endl;
    s.outoutList(v);
}