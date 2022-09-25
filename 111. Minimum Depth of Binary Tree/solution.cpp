/*
Idea: BFS traversal and find the shortest leaf node

Time complexity : O(n)
Space complexity: O(n)
*/

#include<queue>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root)
            return 0;
        
        queue<pair<TreeNode*, int>> q;
        q.push({root, 1});
        
        while(!q.empty()){
            auto [node, path] = q.front(); 
            q.pop();
            
            if(!node->left and !node->right)
                return path;
            
            if(node->left)
                q.push({node->left, path + 1});
            
            if(node->right)
                q.push({node->right, path + 1});
        }
        
        return -1;
    }
};