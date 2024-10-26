/*

	Author: Zofia Marciniak @zosiazamoyska

    There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

    A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

    The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

    Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.

    Link: https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/description/
*/ 
 
 #include <iostream>
 #include <vector>
 #include <queue>
 using namespace std;
 const int N = 100000;
 const int INF = 1000000000+21;
 const int MOD = 1000000000+7;
 
 int n, m, a, b, c;
 vector<pair<int, int> > G[N];
 int dist[N];
 int ans[N];
 
 void dijkstra(int v){
 	
 	priority_queue<pair<int, int> > Q;
 	dist[v] = 0;
 	Q.push(make_pair(0, v));
 	
 	while (!Q.empty())
 	{
 		pair<int, int> curr = Q.top();
 		Q.pop();
 		for (auto &i:G[curr.second])
 		{
 			// v -> w (odl)
 			int w = i.first;
 			int odl = i.second;
 			if (dist[w] > dist[curr.second] + odl)
 			{
 				dist[w] = dist[curr.second] + odl;
 				Q.push(make_pair(-(dist[w]), w));
 			}
 		}
 	}
 }
 
 int dfs(int v)
 {
 	if (ans[v] != -1) // if answer exists
 		return ans[v];
 	if (v == n)
 		return 1;
 	
 	int wynik = 0;
 	for (auto &i:G[v])
 	{
 		 int w = i.first;
 		 if (dist[v] > dist[w])
 			wynik = (wynik + dfs(w)) % MOD;
 	}
	return wynik; 		

 }
 
 int main()
 {
 	cin>>n>>m;
 	for (int i=0; i<m; i++)
 	{
 		cin>>a>>b>>c;
 		G[a].push_back(make_pair(b, c));
 		G[b].push_back(make_pair(a, c));
 	}
 	for (int i=0; i<=n; i++)
 	{
 		dist[i] = INF;
 		ans[i] = -1;
 	}	
 	dijkstra(n);
 	
 	cout<<dfs(1);
 }
 