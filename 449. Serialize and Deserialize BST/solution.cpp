#include<iostream>
#include<climits>
#include<cstring>

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
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string data;
        inOrder(root, data);
        return data;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int pos = 0;
        return decode(data, pos, INT_MIN, INT_MAX);
    }
    
private:
    
    void inOrder(TreeNode* node, string& data){
        if(!node)
            return;
        
        char buffer[4];
        
        memcpy(buffer, &(node->val), sizeof(int));
        for(int i = 0; i < 4; ++i)
            data.push_back(buffer[i]);
        
        inOrder(node->left, data);
        inOrder(node->right, data);
    }
    
    TreeNode* decode(string data, int& pos, int min_val, int max_val){
        if(pos >= data.size())
            return NULL;
        
        int value;
        memcpy(&value, &data[pos], sizeof(int));
        
        if(value < min_val || value > max_val)
            return NULL;
        
        TreeNode* node = new TreeNode(value);
        pos += sizeof(int);
        node->left = decode(data, pos, min_val, value);
        node->right = decode(data, pos, value, max_val);
        return node;
    }
    
};

// Your Codec object will be instantiated and called as such:
// Codec* ser = new Codec();
// Codec* deser = new Codec();
// string tree = ser->serialize(root);
// TreeNode* ans = deser->deserialize(tree);
// return ans;