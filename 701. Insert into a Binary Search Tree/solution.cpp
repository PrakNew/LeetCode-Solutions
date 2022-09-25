/*
    Time complexity : O(n)
    Space complexity: O(n)
*/

class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        
        if(root==NULL)
        {
            TreeNode *temp = new TreeNode(val);
            return temp;
        }
        else if(root->val > val)
            root->left = insertIntoBST(root->left, val);
        else
            root->right = insertIntoBST(root->right, val);
        
        return root;
    }
};