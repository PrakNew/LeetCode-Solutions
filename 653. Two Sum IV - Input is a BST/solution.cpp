/*
    Time complexity : O(n)
    Space complexity: O(n)
*/


#include<deque>
#include<set>
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
    bool findTarget(TreeNode* root, int k) {
        deque<TreeNode*> q = {root};
        set<int> seen = {root->val};
        
        while(!q.empty())
        {
            TreeNode* node = q.front();
            q.pop_front();
            
            if(node->val * 2 != k and seen.count(k - node->val) == 1)
                return true;
            
            if(node->left){
                q.push_back(node->left);
                seen.insert(node->left->val);
            }
            
            if(node->right){
                q.push_back(node->right);
                seen.insert(node->right->val);
            }
        }
        
        return false;
    }
};