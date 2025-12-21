struct Node{
    int val ;
    Node* next;
    Node* prev;
    Node(int val=0){
        this->val =val;
        next = prev =NULL;
    }
};

class MyLinkedList {
    Node* head;
    Node* tail;
    int count ;
public:
    MyLinkedList() {
         head =tail = NULL;
         count = 0;
    }
    int get(int index) {
        if(index < 0 || index >= count)
            return -1;
        Node*curr  = head;
        for(int i = 0 ; i < index ; i++)
            curr= curr->next;
        return curr->val;
        
    }
    void addAtHead(int val) {
        Node* newNode = new Node(val);
        if(head == NULL){
            head = tail = newNode;
            count =1;
            return;
        }
        newNode->next= head;
        head->prev=newNode;
        head =newNode;
        count++;

    }
    
    void addAtTail(int val) {
        Node* newNode = new Node(val);
        if(head == NULL){
            head = tail = newNode;
            count =1;
            return;
        }
        newNode->prev= tail;
        tail->next=newNode;
        tail =newNode;

        count++;

    }
    
    void addAtIndex(int index, int val) {
        if(index > count || index < 0)
            return;
        
        if(index == count){
            addAtTail(val);
            return;
        }
        if(index == 0){
            addAtHead(val);
            return;
        }

        Node* current  =head;
        Node* trailCurrent = nullptr;
        for(int i = 0; i < index;i++){
            trailCurrent= current;
            current = current->next;
        }
        Node* newNode = new Node(val);

        trailCurrent->next = newNode;
        current->prev =newNode;
        newNode->next = current;
        newNode->prev =trailCurrent;

        count++;
        
    }
    
    void deleteAtIndex(int index) {
        if(index >= count || index < 0)
            return;
        
 
        Node* current  =head;
        Node* trailCurrent = nullptr;
        if(index == 0){
            head = head->next;
            if(head != NULL){
                head->prev =NULL;
            }else{
                tail = NULL;
            }
            delete current;
            count --;
            return;
        }
        for(int i = 0; i < index;i++){
            trailCurrent= current;
            current = current->next;
        }

        trailCurrent->next = current->next;
        if(current->next != NULL)
            current->next->prev =trailCurrent;
        
        if(current == tail )
            tail =trailCurrent;
        
        delete current;

        count--;
    
    }

};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */