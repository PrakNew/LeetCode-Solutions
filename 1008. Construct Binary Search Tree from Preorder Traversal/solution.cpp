/*
Time complexity : O(n)
Space complexity: O(n)
*/

#include<vector>
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
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        stack<TreeNode*> st;
        TreeNode* root = new TreeNode(preorder[0]);
        st.push(root);
        int n = preorder.size();
        
        for(int i = 1; i < preorder.size(); ++i){
            int val = preorder[i];
            if(!st.empty() and val < st.top()->val){
                TreeNode* newNode = new TreeNode(val);
                st.top()->left = newNode;
                st.push(newNode);
            }
            
            TreeNode* lastNode = NULL;
            
            while(!st.empty() and st.top()->val < val){
                lastNode = st.top();
                st.pop();
            }
            
            if(lastNode){
                TreeNode* newNode = new TreeNode(val);
                lastNode->right = newNode;
                st.push(newNode);
            }
        }
        
        return root;
    }
};