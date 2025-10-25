import java.util.LinkedList;
import java.util.Queue;
public class QueueExample {
    public static void main(String[] args) {
        Queue<String> q = new LinkedList<>();
        q.add("red");
        q.add("green");
        q.add("blue");
        while(!q.isEmpty()) {
            System.out.println(q.poll());
        }
    }
}
