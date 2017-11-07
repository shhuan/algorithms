/*
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 * You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
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
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;

        int rowNum = grid.size(), colNum = grid[0].size();
        int count = 0;

        set<pair<int, int>> c;
        for (int i = 0; i < rowNum; ++i) {
            for (int j = 0; j < colNum; ++j) {
                c.insert(make_pair(i, j));
            }
        }

        vector<pair<int, int>> delta{{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
        set<pair<int, int>> q;
        while (!c.empty()){
            auto rowCol = *c.begin();
            if (grid[rowCol.first][rowCol.second] == '1'){
                count++;
                q.insert(rowCol);
                while (!q.empty()){
                    rowCol = *q.begin();
                    int row = rowCol.first;
                    int col = rowCol.second;
                    c.erase(rowCol);
                    q.erase(rowCol);
                    if (grid[row][col] == '1'){
                        for (auto d : delta){
                            auto nextRowCol = make_pair(row+d.first, col+d.second);
                            if (grid[nextRowCol.first][nextRowCol.second] == '1' && c.find(nextRowCol) != c.end()){
                                q.insert(nextRowCol);
                            } else{
                                c.erase(nextRowCol);
                            }
                        }
                    }
                }
            } else{
                c.erase(rowCol);
            }
        }

        return count;
    }


    int numIslands2(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        int rowNum = grid.size(), colNum = grid[0].size();
        vector<vector<bool>> visited(rowNum, vector<bool>(colNum, false));

        int count = 0;
        for (int i = 0; i < rowNum; ++i) {
            for (int j = 0; j < colNum; ++j) {
                if (!visited[i][j] && grid[i][j] == '1'){
                    count++;
                    dfs(grid, i, j, visited);
                }
            }
        }
        return count;
    }
        void dfs(vector<vector<char>>& grid, int row, int col, vector<vector<bool>>& visited){
        if (row >= grid.size() || col >= grid[row].size()){
            return;
        }
        vector<pair<int, int>> delta{{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
        if (grid[row][col] == '1' && !visited[row][col]){
            visited[row][col] = true;
            for (auto d : delta){
                dfs(grid, row+d.first, col+d.second, visited);
            }
        }
    }
};

int main(){
    Solution s;
    vector<vector<char>> grid{{'1','1','1','1','0'},
                              {'1','1','0','1','0'},
                              {'1','1','0','0','0'},
                              {'0','0','0','0','0'}
                            };
    cout << s.numIslands(grid) << endl;

    grid = {{'1','1','1','1','0'},
            {'1','1','0','0','0'},
            {'1','1','0','0','0'},
            {'0','0','1','0','0'},
            {'0','0','0','1','1'}
    };
    cout << s.numIslands(grid) << endl;

    grid = {{'1'}};
    cout << s.numIslands(grid) << endl;
}