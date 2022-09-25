#include<iostream>
#include<vector>
#include<deque>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.size()==0)
            return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<bool> > visited(m, vector<bool>(n, false));
        vector<vector<int> > dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int islands = 0;
        
        for(int i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j){
                if(grid[i][j] == '1' && visited[i][j] == false){
                        islands++;
                        visited[i][j] = true;
                        deque<pair<int, int> > queue;
                        queue.push_back({i, j});
                        while(queue.size()){
                            pair<int, int> xy = queue.back();
                            int x = xy.first, y = xy.second;
                            queue.pop_back();
                            for(auto dir: dirs){
                                int r = x + dir[0];
                                int c = y + dir[1];
                                if(0 <= r and r < m and 0 <= c and c < n and visited[r][c] == false and grid[r][c] == '1'){
                                    visited[r][c] = true;
                                    queue.push_back({r, c});
                                }
                            }   
                        }
                                   
                }
            }
        }
        
        return islands;
    }
};