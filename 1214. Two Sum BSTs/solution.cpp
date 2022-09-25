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
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        deque<TreeNode*> q1 = {root1};
        deque<TreeNode*> q2 = {root2};
        set<int> seen = {root1->val};
        
        while(!q1.empty()){
            auto node = q1.front();
            q1.pop_front();
            
            if(node->left){
                seen.insert(node->left->val);
                q1.push_back(node->left);
            }
            if(node->right){
                seen.insert(node->right->val);
                q1.push_back(node->right);
            }
        }
        
        while(!q2.empty()){
            auto node = q2.front();
            q2.pop_front();
            
            if(seen.count(target - node->val))
                return true;
            
            if(node->left)
                q2.push_back(node->left);
            
            if(node->right)
                q2.push_back(node->right);
        }
        
        return false;
    }
};