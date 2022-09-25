/*
Time complexity : O(h + k)
Space complexity: O(h)
*/

#include<stack>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        
        if(p->right){
            TreeNode* temp = p->right;
            while(temp->left)
                temp = temp->left;
            return temp;
        }
        
        stack<TreeNode*> st;
        while(root || !st.empty()){
            while(root){
                st.push(root);
                root = root->left;
            }
            
            root = st.top();
            st.pop();
            if(root->val > p->val)
                return root;
            root = root->right;
        }
        return NULL;
    }
};