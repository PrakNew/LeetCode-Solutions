/*
Idea: Topological sort

Time complexity : O(|e| + |v|)
Space complexity: O(|e| + |v|)
*/
#include<vector>
#include<map>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int n, vector<vector<int>>& courses) {
        map<int, vector<int>> graph;
        vector<bool> visited(n, false);
        vector<bool> recStack(n, false);

        for(auto course: courses){
            int x = course[0], y = course[1];
            graph[y].push_back(x);
        }
        
        // Check for cycles in graph
        for(int x = 0; x < n; ++x){
            if(!visited[x])
                if(isCyclic(graph, x, visited, recStack))
                    return {};
        }
        
        // Topological sort
        vector<int> order;
        for(int i = 0; i < n; ++i)
            visited[i] = false;
        
        for(int x = 0; x < n; ++x)
            if(!visited[x])
                topSort(graph, x, visited, order);        
        
        return order;
    }
private:
    bool isCyclic(map<int, vector<int>>& graph, int node, vector<bool>& visited, vector<bool>& recStack){
        recStack[node] = true;
        visited[node] = true;
        
        for(auto neighbor: graph[node]){
            if(!visited[neighbor])
                if(isCyclic(graph, neighbor, visited, recStack))
                    return true;
            if(recStack[neighbor])
                return true;
        }
        
        recStack[node] = false;
        return false;
    }
    
    void topSort(map<int, vector<int>>& graph, int node, vector<bool>& visited, vector<int>& order){
        visited[node] = true;
        for(auto neighbor: graph[node]){
            if(!visited[neighbor])
                topSort(graph, neighbor, visited, order);
        }
        order.insert(begin(order), node);
    }
};