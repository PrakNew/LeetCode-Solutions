/*
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        
        if(!root)
            return res;
        
        queue<TreeNode*> q;
        q.push(root);
        vector<int> level;
        
        while(!q.empty()){
            int size = q.size();
            level.clear();
            
            while(size--){
                TreeNode* node = q.front(); 
                q.pop();
                level.push_back(node->val);
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right);
            }
            res.push_back(level);
        }
        
        reverse(begin(res), end(res));
        return res;
    }
};