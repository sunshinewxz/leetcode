import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by apple on 18-6-5.
 */
public class MyStack {
    Queue<Integer> q;
    /** Initialize your data structure here. */
    public MyStack() {
        q = new LinkedList<>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        q.offer(x);
        for(int i = 1; i <= q.size()-1; i++)
            q.offer(q.poll());
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int element = q.element();
        q.poll();
        return element;
    }

    /** Get the top element. */
    public int top() {
        return q.element();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return q.size()==0;
    }
}
