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
    bool isSymmetric(TreeNode* root) {
        return mirror(root, root);
    }
private:
    bool mirror(TreeNode* t1, TreeNode* t2){
        if(!t1 and !t2)
            return true;
        if(!t1 || !t2)
            return false;
        if(t1->val != t2->val)
            return false;
        
        return mirror(t1->left, t2->right) and mirror(t1->right, t2->left);
    }
};