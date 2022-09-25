/*
Time complexity : O(n)
Space complexity: O(n)
*/

#include<vector>
#include<map>
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        map<int, int> indexOf;
        int n = postorder.size();
        deque<int> dq(begin(postorder), end(postorder));
        for(int i = 0; i < n; ++i)
            indexOf[inorder[i]] = i;
        
        return util(0, n-1, indexOf, dq);
    }
private:
    TreeNode* util(int lo, int hi, map<int, int>& indexOf, deque<int>& postorder){
        if(lo > hi)
            return NULL;
        
        int val = postorder.back();
        postorder.pop_back();
        int mid = indexOf[val];
        
        TreeNode* node = new TreeNode(val);
        node->right = util(mid + 1, hi, indexOf, postorder);
        node->left = util(lo, mid - 1, indexOf, postorder);
        
        return node;
    }
};