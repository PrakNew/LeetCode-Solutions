#include<iostream>
#include<vector>
#include<deque>
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
    bool isEvenOddTree(TreeNode* root) {
        deque<TreeNode*> q;
        q.push_back(root);
        int level = 0;
        int prev;
        while(q.size()){
            int size = q.size();
            vector<TreeNode*> nodes;
            while(size--){
                TreeNode* node = q[0];
                q.pop_front();
                nodes.push_back(node);
                if(node->left)
                    q.push_back(node->left);
                if(node->right)
                    q.push_back(node->right);
            }
            
            // Odd levels - strictly decreasing even integers 
            if(level&1){
                printf("%d\n", level);
                if((nodes[0]->val & 1) != 0)
                    return false;
                for(int i = 1; i < nodes.size(); ++i)
                    if( (nodes[i]->val & 1) != 0 || nodes[i]->val >= nodes[i-1]->val)
                        return false;
            }
            // even levels - strictly increasing odd integers 
            else{
                printf("%d\n", level);
                if((nodes[0]->val & 1) == 0)
                    return false;
                for(int i = 1; i < nodes.size(); ++i)
                    if( (nodes[i]->val & 1) == 0 || nodes[i]->val <= nodes[i-1]->val)
                        return false;
            }
            level++;
        }
        
        return true;
    }
};