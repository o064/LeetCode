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
        if(head == NULL || head->next == NULL)
            return head;
        ListNode* dummyHead = new ListNode(0,head);
        ListNode* prev = dummyHead;
        ListNode* curr =dummyHead->next;
        ListNode* next =dummyHead->next->next;
        int lastDeleted = -999;
        while(next != NULL){

            if(lastDeleted == curr->val ||next->val == curr->val ){
                lastDeleted =curr->val;
                prev->next= curr->next;
                delete curr;
                curr = next;
                next= next->next;
            }else{
                curr = curr->next;
                prev = prev->next;
                next= next->next;
            }
        }
        if(lastDeleted == curr->val ){
            prev->next= curr->next;
            delete curr;

        }
        return dummyHead->next;
    }
};