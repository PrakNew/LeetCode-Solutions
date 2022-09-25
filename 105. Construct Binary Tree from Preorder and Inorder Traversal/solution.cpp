/*
Time complexity : O(n)
Space complexity: O(n)
*/

#include<vector>
#include<deque>
#include<map>
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = inorder.size();
        map<int, int> indexOf;
        deque<int> dq(begin(preorder), end(preorder));
        for(int i = 0; i < n; ++i)
            indexOf[inorder[i]] = i;
        
        return util(0, n -1, dq, indexOf);
    }
private:
    TreeNode* util(int lo, int hi, deque<int>& preorder, map<int, int>& indexOf){
        if(lo > hi)
            return NULL;
        
        int val = preorder.front();
        preorder.pop_front();
        int mid = indexOf[val];
        
        TreeNode* node = new TreeNode(val);
        node->left = util(lo, mid - 1, preorder, indexOf);
        node->right = util(mid + 1, hi, preorder, indexOf);
        
        return node;
    }
};