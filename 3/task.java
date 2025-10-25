import java.util.*;

public class task {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>(Arrays.asList(5, 2, 8, 1, 3));
        System.out.println("Массив: " + numbers);
        numbers.add(10);
        numbers.remove(1);
        Collections.sort(numbers);
        System.out.println("После изменений: " + numbers);
        System.out.println();

        Stack<Integer> stack = new Stack<>();
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println("Стек: " + stack);
        stack.pop();
        System.out.println("После pop: " + stack);
        System.out.println();

        Queue<String> queue = new LinkedList<>();
        queue.add("Петя");
        queue.add("Вася");
        queue.add("Маша");
        System.out.println("Очередь: " + queue);
        queue.poll();
        System.out.println("После обслуживания: " + queue);
        System.out.println();

        Deque<Integer> d = new ArrayDeque<>();
        d.addLast(1);
        d.addLast(2);
        d.addFirst(0);
        System.out.println("Дек: " + d);
        d.pollLast();
        d.pollFirst();
        System.out.println("После pop: " + d);
        System.out.println();

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.add(new int[]{2, 0});
        pq.add(new int[]{1, 1});
        pq.add(new int[]{3, 2});
        String[] names = {"Вася", "Петя", "Маша"};
        System.out.println("Приоритетная очередь:");
        while (!pq.isEmpty()) {
            int[] x = pq.poll();
            System.out.println(names[x[1]]);
        }
        System.out.println();

        class Node {
            String data;
            Node next;
            Node(String d) { data = d; }
        }
        Node head = new Node("Петя");
        head.next = new Node("Вася");
        head.next.next = new Node("Маша");
        System.out.print("Связный список: ");
        Node t = head;
        while (t != null) {
            System.out.print(t.data + " -> ");
            t = t.next;
        }
        System.out.println("None");
        System.out.println();

        Map<String, List<Integer>> multi = new HashMap<>();
        multi.put("Петя", Arrays.asList(5, 4, 3));
        multi.put("Маша", Arrays.asList(4, 5, 5));
        multi.put("Вася", Arrays.asList(3, 3, 4));
        for (String k : multi.keySet()) {
            List<Integer> marks = multi.get(k);
            double avg = marks.stream().mapToInt(Integer::intValue).average().orElse(0);
            System.out.println(k + ": " + marks + " средний " + avg);
        }
    }
}
