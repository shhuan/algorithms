/*
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
 */

#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>

using namespace std;

class Solution {
public:
    int findMin(vector<int> &nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        int l = 0;
        int r = nums.size() - 1;
        while (l < r) {
            if (nums[l] < nums[r]) {
                return nums[l];
            }
            int m = l + (r - l) / 2;
            if (m == l) {
                return min(nums[m], nums[m + 1]);
            } else if (nums[m] < nums[l]) {
                r = m;
            } else {
                l = m;
            }
        }
        return -1;
    }
};

int main() {
    vector<int> nums{4, 5, 6, 7, 0, 1, 2};
    Solution s;
    cout << s.findMin(nums) << endl;
}