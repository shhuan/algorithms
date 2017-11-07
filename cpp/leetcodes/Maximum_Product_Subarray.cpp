/*
 * Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
 */

#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int> &nums) {
        if (nums.empty()) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }
        int left = -1;
        int res = INT32_MIN;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 0) {
                res = max(res, 0);
                if (left >= 0) {
                    res = max(res, maxProductInGroup(nums, left, i));
                    left = -1;
                }
            } else {
                if (left < 0) {
                    left = i;
                }
            }
        }
        if (left >= 0 && left < nums.size()) {
            res = max(res, maxProductInGroup(nums, left, nums.size()));
        }
        return res;
    }

    int maxProductInGroup(vector<int> &nums, int left, int right) {
        if (left == right - 1) {
            return nums[left];
        }
        int firstNegative = -1;
        int lastNegative = -1;
        int negativeCount = 0;
        for (int i = left; i < right; i++) {
            if (nums[i] < 0) {
                if (firstNegative < 0) {
                    firstNegative = i;
                    lastNegative = i;
                } else {
                    lastNegative = i;
                }
                negativeCount++;
            }
        }
        if ((negativeCount & 1) == 0) {
            int product = 1;
            for (int i = left; i < right; ++i) {
                product *= nums[i];
            }
            return product;
        } else {
            int p1 = 1;
            for (int i = left; i < lastNegative; ++i) {
                p1 *= nums[i];
            }
            int p2 = 1;
            for (int j = firstNegative + 1; j < right; ++j) {
                p2 *= nums[j];
            }
            return max(p1, p2);
        }
    }

};

void test(vector<int> &nums, int expect) {
    Solution s;
    int res = s.maxProduct(nums);
    if (res == expect) {
        cout << "Pass!" << endl;
    } else {
        cout << "Fail!, expect: " << expect << ", actual: " << res << endl;
    }
}

int main() {
    Solution s;
    auto v = vector<int>{2, 3, -2, 4};
    test(v, 6);
    v = vector<int>{2, 3, -2, -2, -2};
    test(v, 24);
    v = vector<int>{-1};
    test(v, -1);
    v = vector<int>{0};
    test(v, 0);
    v = vector<int>{-3, -4};
    test(v, 12);
    v = vector<int>{-3, 0, -3};
    test(v, 0);

}