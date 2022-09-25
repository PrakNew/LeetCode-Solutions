/*
Idea: Perform BFS from every node i and populate isReachable[i][j] matrix.

Time complexity : O(|v|^2)
Space complexity: O(|v|^2)
*/
#include<vector>
#include<map>
#include<queue>
using namespace std;

class Solution {
public:
    vector<bool> checkIfPrerequisite(int n, vector<vector<int>>& courses, vector<vector<int>>& queries) {
        map<int, vector<int>> graph;

        for(auto course: courses){
            int x = course[0], y = course[1];
            graph[x].push_back(y);
        }
        
        vector<vector<bool>> isReachable(n, vector<bool> (n, false));
        
        for(int i = 0; i < n; ++i){
            queue<int> q;
            q.push(i);
            vector<bool> visited(n, false);
            visited[i] = true;
            while(q.size()){
                auto node = q.front();
                q.pop();
                isReachable[i][node] = true;
                for(auto neighbor : graph[node]){
                    if(!visited[neighbor]){
                        visited[neighbor] = true;
                        q.push(neighbor);
                    }
                }
            }
        }
        
        vector<bool> res;
        for(auto query: queries){
            int a = query[0], b = query[1];
            res.push_back(isReachable[a][b]);
        }
        
        return res;
    }
};