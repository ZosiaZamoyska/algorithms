/*
	Author: Zofia Marciniak @zosiazamoyska

    Finding tree's diameter using 2 DFS
*/

#include <iostream>
#include <vector>
using namespace std;
const int N = 1000000+21;
vector<int> tab[N];
int dis[N][2];
int n, a, b;
int dfs(int v, int p, int d, int dlu)
{
	dis[v][dlu] = d;
	int node = -1;
	for (int i=0; i<tab[v].size(); i++)
	{
		int w = tab[v][i];
		if (w != p)
		{
			int x = dfs(w, v, d+1, dlu);
			if (node == -1 || dis[x][dlu] > dis[node][dlu]) node = x;
		}
	}
	if (node == -1)
		return v;
	return node;
}

int main() {
	cin>>n;
	
	for (int i=0; i<n; i++)
	{
		cin>>a>>b;
		tab[a].push_back(b);
		tab[b].push_back(a);
	}
	
	int A = dfs(1, 1, 0, 0);
	int B = dfs(A, A, 0, 0);

    cout<<"Diameter is from "<<A<<" to "<<B<<endl;

	return 0;
}