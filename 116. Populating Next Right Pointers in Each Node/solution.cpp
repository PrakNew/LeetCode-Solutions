/*
Time complexity : O(n)
Space complexity: O(1)
*/

#include<vector>
using namespace std;

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if(!root)
            return NULL;
        
        Node* current = root;
        
        while(current->left){
            Node* leftMostChild = current->left;
            while(current){
                current->left->next = current->right;
                current->right->next = current->next ? current->next->left : NULL;
                current = current->next;
            }
            current = leftMostChild;
        }
        
        return root;
    }
};