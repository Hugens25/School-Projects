// Arup Guha
// 10/8/2015
// Kruskal's Algorithm - written as an example for the programming team.
// Greedy algorithm for connecting nodes in shortest paths.

import java.util.*;

class djset {

	public int[] parent;

	// Creates a disjoint set of size n (0, 1, ..., n-1)
	public djset(int n) {
		parent = new int[n];
		for (int i=0; i<n; i++)
			parent[i] = i;
	}

	public int find(int v) {

		// I am the club president!!! (root of the tree)
		if (parent[v] == v) return v;

		// Find my parent's root.
		int res = find(parent[v]);

		// Attach me directly to the root of my tree.
		parent[v] = res;
		return res;
	}

	public boolean union(int v1, int v2) {

		// Find respective roots.
		int rootv1 = find(v1);
		int rootv2 = find(v2);

		// No union done, v1, v2 already together.
		if (rootv1 == rootv2) return false;

		// Attach tree of v2 to tree of v1.
		parent[rootv2] = rootv1;
		return true;
	}
}


class edge implements Comparable<edge> {

	public int v1;
	public int v2;
	public int w;

	public edge(int a, int b, int weight) {
		v1 = a;
		v2 = b;
		w = weight;
	}

	public int compareTo(edge other) {
		return this.w - other.w;
	}
}

class kruskals {

	public static int mst(edge[] list, int n) {
		Arrays.sort(list);

		djset trees = new djset(n);
		int numEdges = 0, res = 0;

		// Consider edges in order.
		for (int i=0; i<list.length; i++) {

			// Try to put together these two trees.
			boolean merged = trees.union(list[i].v1, list[i].v2);
			if (!merged) continue;

			// Bookkeepping.
			numEdges++;
			res += list[i].w;
			if (numEdges == n-1) break;
		}

		// -1 indicates no MST, so not connected.
		return numEdges == n-1 ? res : -1;
	}
}
