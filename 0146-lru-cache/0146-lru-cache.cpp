struct Node {
    int key, value;
    Node* prev;
    Node* next;
    Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
};

class LRUCache {
    unordered_map<int, Node*> mp;
    Node* head;
    Node* tail;
    int capacity;
    void remove(Node* node){
        if(node->prev) node->prev->next= node->next;
        else head = node->next;
        if(node->next) node->next->prev = node->prev;
        else tail =node->prev;
    }
    void append(Node* node){
        node->prev = tail;
        node->next = nullptr;

        if(tail) tail->next=node;
        tail =node;
        
        if(!head) head = node;
    }
public:
    LRUCache(int capacity) {
        head = tail =nullptr;
        this->capacity =capacity;
    }
    
    int get(int key) {
        if(!mp.count(key)) return -1;
        Node *node =mp[key];

        remove(node);
        append(node);

        return node->value;
        
    }
    
    void put(int key, int value) {

        if(mp.count(key)){
            Node* node = mp[key];
            node->value =value;
            remove(node);
            append(node); 
        }else{
            if(mp.size() == capacity){
                mp.erase(head->key);
                remove(head);
            }
            Node *node = new Node(key,value);
            append(node);
            mp[key] = node;

        }
        
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */