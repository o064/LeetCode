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
        Node* copyHead = new Node(0);
        auto curr = head; 
        auto currCopy =copyHead;
        unordered_map<Node* , Node*> mp;
        while(curr){
            auto newNode= new Node(curr->val);
            newNode->next = curr->next;
            mp[curr] =  newNode ; 
            currCopy->next = newNode ;
            currCopy = currCopy->next;
            curr = curr->next;
        }
        currCopy = copyHead->next;
        curr = head; 
        while(currCopy){
            auto it = mp.find(curr->random);
            if(it != mp.end()){
                currCopy->random = it->second;
            }else{
                currCopy->random = nullptr;

            }
            currCopy = currCopy->next;
            curr = curr->next;
        }

        return copyHead->next;
    }
};