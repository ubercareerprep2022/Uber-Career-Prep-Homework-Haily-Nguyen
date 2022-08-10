/**
 * GRAPH TRAVERSAL EXERCISES
 * Haily Nguyen UCP 2022
 * Ex2 + Ex3 + Ex4 + Ex5
 */

import java.io.*;
import java.util.*;

// This class represents a directed graph using adjacency list representation
class GraphWithAdjacencyList {
    private int V; // No. of vertices

    // Array  of lists for
    // Adjacency List Representation
    private static LinkedList<Integer>[] adj;

    // Constructor
    GraphWithAdjacencyList(int v)
    {
        V = v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; ++i)
            adj[i] = new LinkedList();
    }

    // Function to add an edge into the graph
    void addEdge(int v, int w)
    {
        adj[v].add(w); // Add w to v's list.
    }

    // Helper function for DFS
    void DFSUtil(int v, boolean visited[])
    {
        // Mark the current node as visited and print it
        visited[v] = true;
        System.out.print(v + " ");

        // Recurse through all vertices adjacent to this vertex
        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited[n])
                DFSUtil(n, visited);
        }
    }

    // [Graphs - Ex2] Exercise: DFS Traversal
    // Recursion
    void DFS(int v)
    {
        // Mark all the vertices as not visited (set as false by default in java)
        boolean visited[] = new boolean[V];

        // Call the recursive helper function to print DFS traversal
        DFSUtil(v, visited);
    }

    // [Graphs - Ex3] Exercise: BFS Traversal
    public void BFS(int s)
    {
        // Mark all the vertices as not visited
        boolean visited[] = new boolean[V];

        // Create a queue for BFS
        LinkedList<Integer> queue = new LinkedList<Integer>();

        // Mark the current node as visited and enqueue it
        visited[s]=true;
        queue.add(s);

        while (queue.size() != 0)
        {
            // Dequeue a vertex from queue and print it
            s = queue.poll();
            System.out.print(s+" ");

            // Get all adjacent vertices of the dequeued vertex s
            // If an adjacent vertex has not been visited, then mark it visited and enqueue it
            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext())
            {
                int n = i.next();
                if (!visited[n])
                {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }

    // [Graphs - Ex4] Exercise: Minimum number of edges between two nodes of a Graph
    static int minEdgeBFS(int u, int v, int n)
    {
        // visited[n] for keeping track of visited node in BFS
        Vector<Boolean> visited = new Vector<Boolean>(n);

        for (int i = 0; i < n; i++) {
            visited.addElement(false);
        }

        // Initialize distance as 0
        Vector<Integer> distance = new Vector<Integer>(n);

        for (int i = 0; i < n; i++) {
            distance.addElement(0);
        }

        // Queue to do BFS.
        Queue<Integer> Q = new LinkedList<>();
        distance.setElementAt(0, u);

        Q.add(u);
        visited.setElementAt(true, u);
        while (!Q.isEmpty()) {
            int x = Q.peek();
            Q.poll();

            for (int i=0; i<adj[x].size(); i++)
            {
                if (visited.elementAt(adj[x].get(i)))
                    continue;

                // update distance for i
                distance.setElementAt(distance.get(x) + 1,adj[x].get(i));
                Q.add(adj[x].get(i));
                visited.setElementAt(true,adj[x].get(i));
            }
        }
        return distance.get(v);
    }

    // [Graphs - Ex5] Exercise: Loop in a Directed Graph
    private boolean isLoopUtil(int i, boolean[] visited, boolean[] recStack)
    {
        // Mark the current node as visited and part of recursion stack
        if (recStack[i])
            return true;

        if (visited[i])
            return false;
        visited[i] = true;
        recStack[i] = true;

        List<Integer> children = adj[i];

        for (Integer c: children)
            if (isLoopUtil(c, visited, recStack))
                return true;

        recStack[i] = false;
        return false;
    }

    private boolean isLoop()
    {
        // Mark all the vertices as not visited and not part of recursion stack
        boolean[] visited = new boolean[V];
        boolean[] recStack = new boolean[V];

        // Call the recursive helper function to detect cycle in different DFS trees
        for (int i = 0; i < V; i++)
            if (isLoopUtil(i, visited, recStack))
                return true;

        return false;
    }

    // Driver Code
    public static void main(String args[])
    {
        GraphWithAdjacencyList g = new GraphWithAdjacencyList(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        System.out.println("Following is Depth First Search Traversal "
                        + "(starting from vertex 2)");

        g.DFS(2);
        System.out.println("\nFollowing is Breadth First Search Traversal "
                + "(starting from vertex 2)");

        g.BFS(2);

        System.out.println("\nMin edges BFS between 1 and 3:");
        System.out.println(minEdgeBFS(1, 3, 4));

        if(g.isLoop())
            System.out.println("Graph contains cycle");
        else
            System.out.println("Graph doesn't "
                    + "contain cycle");
    }
}
