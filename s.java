import java.util.*;

public class s {

    public static List<Integer> getImpactedDevices(int[][] edges, int targetDevice) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Set<Integer> visited = new HashSet<>();
        List<Integer> impactedDevices = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        // Build the adjacency list representation of the network connections
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            graph.putIfAbsent(u, new ArrayList<>());
            graph.get(u).add(v);
            graph.putIfAbsent(v, new ArrayList<>());
            graph.get(v).add(u);
        }

        // Perform BFS to find impacted devices
        queue.offer(targetDevice);
        visited.add(targetDevice);

        while (!queue.isEmpty()) {
            int currentDevice = queue.poll();

            // Traverse all connected devices
            if (graph.containsKey(currentDevice)) {
                for (int neighbor : graph.get(currentDevice)) {
                    if (!visited.contains(neighbor)) {
                        queue.offer(neighbor);
                        visited.add(neighbor);
                        impactedDevices.add(neighbor);
                    }
                }
            }
        }

        return impactedDevices;
    }

    public static void main(String[] args) {
        int[][] edges = {{0,1},{0,2},{1,3},{1,6},{2,4},{4,6},{4,5},{5,7}};
        int targetDevice = 4;
        List<Integer> impactedDevices = getImpactedDevices(edges, targetDevice);
        Collections.sort(impactedDevices);
        System.out.println("Impacted Device List: " + impactedDevices); // Output: [5, 7]
    }
}