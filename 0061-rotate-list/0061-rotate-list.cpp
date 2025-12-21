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
    ListNode* rotateRight(ListNode* head, int k) {
        if(k == 0 || !head)
            return head;
        ListNode *fast =head;
        ListNode *slow = head;
        int count = 0 ;
        ListNode *curr = head;

        while(curr){
            count +=1;
            curr =curr->next;
        }
        k = k% count;
        while(k){
            if(fast->next)
                fast =fast->next;
            else{
                fast =head;
            }
            k--;
        }
        while(fast->next){
            fast = fast->next;
            slow = slow->next;
        }
        fast->next = head;
        head =slow->next;
        slow->next= NULL;

        return head;
    }
};