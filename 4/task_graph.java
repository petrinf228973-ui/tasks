import java.util.*;

public class task_graph {
    static Map<String, List<String[]>> g = new HashMap<>();
    static {
        g.put("A", Arrays.asList(new String[]{"B","1"}, new String[]{"C","4"}));
        g.put("B", Arrays.asList(new String[]{"A","1"}, new String[]{"C","2"}, new String[]{"D","5"}));
        g.put("C", Arrays.asList(new String[]{"A","4"}, new String[]{"B","2"}, new String[]{"D","1"}));
        g.put("D", Arrays.asList(new String[]{"B","5"}, new String[]{"C","1"}));
    }

    static Map<String, Integer> dijkstra(String start) {
        Map<String, Integer> dist = new HashMap<>();
        for (String v : g.keySet()) dist.put(v, Integer.MAX_VALUE);
        dist.put(start, 0);
        PriorityQueue<String[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> Integer.parseInt(a[0])));
        pq.add(new String[]{"0", start});
        while (!pq.isEmpty()) {
            String[] cur = pq.poll();
            int cd = Integer.parseInt(cur[0]);
            String u = cur[1];
            if (cd > dist.get(u)) continue;
            for (String[] edge : g.get(u)) {
                String v = edge[0];
                int w = Integer.parseInt(edge[1]);
                int nd = dist.get(u) + w;
                if (nd < dist.get(v)) {
                    dist.put(v, nd);
                    pq.add(new String[]{String.valueOf(nd), v});
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        Map<String,Integer> res = dijkstra("A");
        for (String k : res.keySet())
            System.out.println(k + ": " + res.get(k));
    }
}
