/*
Time complexity : O(n)
Space complexity: O(n)
*/

#include<vector>
#include<map>
using namespace std;

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(!node)
            return node;
        
        map<Node*, Node*> hash;
        Node* nodeCopy = new Node(node->val);
        Node* neighborCopy = NULL;
        hash[node] = nodeCopy;
        deque<Node*> q = {node};
        
        while(!q.empty()){
            node = q.front();   q.pop_front();
            for(auto neighbor : node->neighbors){
                if(hash.find(neighbor) == hash.end()){
                    neighborCopy = new Node(neighbor->val);
                    hash[neighbor] = neighborCopy;
                    hash[node]->neighbors.push_back(neighborCopy);
                    q.push_back(neighbor);
                }
                else
                    hash[node]->neighbors.push_back(hash[neighbor]);
            }
        }
        
        return nodeCopy;
    }
};