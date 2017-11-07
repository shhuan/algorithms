/*
 * There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to
 its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
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
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        if (gas.empty() || cost.empty()){
            return -1;
        }

        int start = 0;
        int len = gas.size();
        while (start < len){
            int remainGas = gas[start];
            int end = (start+1) % len;
            bool finished = true;
            while (end != start){
                remainGas -= cost[(end-1+len)%len];
                if (remainGas < 0){
                    //Caution!!! not start=end
                    start = (end-1+len)%len;
                    finished = false;
                    break;
                }
                remainGas += gas[end];
                end = (end+1) % len;
            }
            if (finished && remainGas >= cost[(end-1+len)%len]){
                return start;
            }
            //Caution!!!
            start++;
        }
        return -1;
    }
};

int main(){
    Solution s;
    vector<int> gas = {2, 3, 4, 2, 1};
    vector<int> cost = {3, 2, 2, 2, 2};
    cout << s.canCompleteCircuit(gas, cost) << endl;

    gas = {2};
    cost = {2};
    cout << s.canCompleteCircuit(gas, cost) << endl;

    gas = {2};
    cost = {3};
    cout << s.canCompleteCircuit(gas, cost) << endl;

    gas = {2, 3};
    cost = {2, 2};
    cout << s.canCompleteCircuit(gas, cost) << endl;

    gas = {2, 3};
    cost = {3, 2};
    cout << s.canCompleteCircuit(gas, cost) << endl;

    gas = {31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30};
    cost = {36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35};
    cout << s.canCompleteCircuit(gas, cost) << endl;
}