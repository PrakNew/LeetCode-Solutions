/*
Time complexity : O(n)
Space complexity: O(n)
*/

#include<iostream>
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
    bool isValidBST(TreeNode* root) {
        return validate(root, NULL, NULL);
    }
private:
    bool validate(TreeNode* root, TreeNode* min, TreeNode* max){
        if(!root)
            return true;
        
        if((min and root->val <= min->val) || (max and root->val >= max->val))
            return false;
        
        return validate(root->left, min, root) and validate(root->right, root, max);
    }
};