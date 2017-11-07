/*
 *
 * Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.

 */
#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>

using namespace std;

class Solution {
public:
    int countDigitOne(int n) {
        int ret = 0;
        if (n <= 0) return ret;
        int num = n;
        int digit = 1;
        while (num) {
            int mod = num % 10;
            int cnt = num / 10;
            int add = mod > 0 ? 1 : 0;

            int normal_appr_cnt = cnt * digit;
            int additional_appr_cnt;
            if (mod == 1)
                additional_appr_cnt = add * (n % digit + 1);
            else
                additional_appr_cnt = add * digit;
            ret += normal_appr_cnt + additional_appr_cnt;

            num /= 10;
            digit *= 10;
        }
        return ret;

    }
};

void test(int val, int expect) {
    Solution s;
    int res = s.countDigitOne(val);
    if (res == expect) {
        cout << "Success" << endl;
    } else {
        cout << "False expect: " << expect << " actual: " << res << endl;
    }
}

int main() {
    test(1, 1);
    test(0, 0);
    test(9, 1);
    test(10, 2);
    test(19, 11);
    test(100, 19);
//    test(123, )

}