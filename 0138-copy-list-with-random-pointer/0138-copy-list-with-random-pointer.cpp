/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        auto curr = head; 
        while(curr){

            auto copy = new Node(curr->val);

            copy->next = curr->next;
            curr->next = copy;

            curr =curr->next->next;
        }

        curr =head;

        while(curr){
            if(curr->random)
                curr->next->random = curr->random->next;
            curr =curr->next->next;
        }

        auto dummy = new Node(0);
        auto copy = dummy;
        curr =head;

        while(curr){
            copy->next = curr->next;
            curr->next = curr->next->next;

            curr =curr->next;
            copy = copy->next;

        }

        return dummy->next;
    }
};