/*
 * There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

click to show more hints.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
 */

#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>
#include <map>
#include <queue>

using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {

        map<int, int> degree;
        map<int, vector<int> > graph;
        for (auto p : prerequisites) {
            int t = p.first;
            int s = p.second;
            if (graph.count(s) <= 0){
                graph[s] = vector<int>();
            }
            graph[s].push_back(t);
            if (degree.find(t) == degree.end()){
                degree[t] = 0;
            }
            degree[t]++;
        }

        queue<int> q;
        std::vector<int> x(numCourses);
        std::iota(std::begin(x), std::end(x), 0); //0 is the starting number
        for (int i : x){
            if (degree.find(i) == degree.end()){
                q.push(i);
            }
        }
        vector<bool> finished(numCourses);
        fill(finished.begin(), finished.end(), false);
        while (!q.empty()) {
            int c = q.front();
            q.pop();
            finished[c] = true;
            for(int nc : graph[c]){
                degree[nc]--;
                if (degree[nc] <= 0){
                    q.push(nc);
                }
            }
        }
        return find(finished.begin(), finished.end(), false) == finished.end();
    }
};


int main(){
    Solution s;
    vector<pair<int, int> >  p{make_pair(1, 0), make_pair(0, 1)};
    cout << s.canFinish(2, p) << endl;
}