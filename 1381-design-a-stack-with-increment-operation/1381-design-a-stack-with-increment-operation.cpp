class CustomStack {
    int size ;
    int*list;
    int top ;

public:
    CustomStack(int maxSize) {
        size = maxSize;
        list = new int[size];
        top = 0;
    }
    
    void push(int x) {
        if(top == size)
            return;
        list[top] = x;
        top++;
    }
    
    int pop() {
        if(top == 0)
            return -1;
        int v = list[top-1];
        top--;
        return v;
    }
    
    void increment(int k, int val) {
        if(k > top)
            k = top ;
        for(int i =0 ; i<k ; i++){
            list[i] += val;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */