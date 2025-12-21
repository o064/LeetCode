/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummyHead = new ListNode(0,head);
        ListNode* prev = dummyHead;
        ListNode* curr =head;
        while(curr){
            
            bool isDuplicated = false;

            while(curr->next && curr->next->val == curr->val){
                isDuplicated= true;

                ListNode* temp =curr;
                curr = curr->next;
                delete temp;
            }
            if(isDuplicated){
                ListNode* temp =curr;
                curr = curr->next;
                delete temp;
                prev->next =curr;
            }else{
                prev =curr;
                curr =curr->next;

            }



        }
        return dummyHead->next;
    }
};