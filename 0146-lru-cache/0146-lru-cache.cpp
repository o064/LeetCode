struct Node{
    int key;
    int value;
    Node* prev;
    Node* next;
    Node(int key ,int value){
        this->key=key;
        this->value =value;
        prev = next = nullptr;
    }
};

class LRUCache {
    unordered_map<int, Node*> mp;
    Node* head; 
    Node* tail;
    int capacity; 
    // remove to the list 
    void remove(Node* node){
        if(node->prev) node->prev->next = node->next;
        else head  = node->next;
        if(node->next) node->next->prev =node->prev;
        else tail = node->prev;

    }
    void append(Node* node){
        node->prev = tail;
        node->next = nullptr;

        if(tail) tail->next =node;
        tail = node;
        if(!head) head = node;
    }
public:
    LRUCache(int capacity) {
        this->capacity =capacity;
        head =tail = nullptr;
    }

    
    int get(int key) {
    // get the value of key if exist else -1  
        if(!mp.count(key))
            return -1; 
        Node* node = mp[key];
        remove(node);
        append(node);
        return node->value;
    }
    
    void put(int key, int value) {
        // update value of if exist else add to cache
        // if capacity exceeded  remove the least recently used
        if(mp.count(key)){
            Node *node =mp[key];
            node->value =value;
            remove(node);
            append(node);
        }else{
            if(mp.size() == capacity){
                mp.erase(head->key);
                remove(head);
            }
            Node* newNode = new Node(key,value);
            append(newNode);
            mp[key]= newNode;

        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */