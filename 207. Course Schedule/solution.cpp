/*
Idea: DFS

Time complexity : O(|e| + |v|)
Space complexity: O(|e| + |v|)
*/
#include<vector>
#include<map>
using namespace std;


class Solution {
public:
    bool canFinish(int n, vector<vector<int>>& courses) {
        vector<bool> visited(n, false);
        vector<bool> recStack(n, false);
        map<int, vector<int>> graph;
        for(auto course: courses){
            int x = course[0], y = course[1];
            graph[y].push_back(x);
        }
        
        for(auto x: graph)
            if(!visited[x.first])
                if(isCyclic(graph, x.first, visited, recStack))
                    return false;
        
        return true;
    }
private:
    bool isCyclic(map<int, vector<int>>& graph, int x, vector<bool>& visited, vector<bool>& recStack){
        recStack[x] = true;
        visited[x] = true;
        
        for(auto neighbor: graph[x]){
            if(!visited[neighbor])
                if(isCyclic(graph, neighbor, visited, recStack))
                    return true;
            if(recStack[neighbor])
                return true;
        }
        
        recStack[x] = false;
        return false;
    }
};