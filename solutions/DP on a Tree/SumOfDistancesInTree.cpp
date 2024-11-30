/*
    Sum of Distances in Tree

    https://leetcode.com/problems/sum-of-distances-in-tree/description/
*/

#include <iostream>
#include <vector>
using namespace std;
const int N = 100000+21;
vector<int> graph[N];
int dp[N][2];
int size[N];
int n, a, b;
int answer = 0;
void dfs1(int v, int prev)
{
    for (int i=0; i<graph[v].size(); i++)
    {
        int u = graph[v][i];
        if (u != prev)
        {
            dfs1(u, v);
            size[v] += size[u];
            dp[v][0] += dp[u][0] + size[u];
        }
    }
    size[v]++;

}

void dfs2(int v, int prev, int prev_val)
{
    dp[v][1] = dp[v][0] + prev_val + (n - size[v]);

    for (int i=0; i<graph[v].size(); i++)
    {
        int u = graph[v][i];
        if (u != prev)
        {
            dfs2(u, v, dp[v][1] - dp[u][0] - size[u]);
        }
    }
    size[v]++;

}
int main()
{
    cin>>n;
    for (int i=1; i<n; i++)
    {
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    dfs1(0, -1);
    dfs2(0, -1, 0);
    for (int i=0; i<n; i++)
	    cout<<dp[i][1]<<endl;
}