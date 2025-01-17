/*
    Given a tree consisting of N Nodes and N-1 edges. 
    The task is to select the maximum set of edges such that each vertex is part of at most one of the selected edges (no two edges share a common end point) 
    i.e., if we select an edge connecting vertex u and v, then we cannot select any other edge connected by vertex u or vertex v.
*/

#include <iostream>
#include <vector>
using namespace std;
const int N = 100000+21;
vector<int> graph[N];
int dp[N][2];
int n, a, b;
int answer = 0;
void dp_tree(int v, int prev)
{
    for (int i=0; i<graph[v].size(); i++)
    {
        int u = graph[v][i];
        if (u != prev)
        {
            dp_tree(u, v);
            dp[v][0] += max(dp[u][0], dp[u][1]);
        }
    }

    for (int i=0; i<graph[v].size(); i++)
    {
        int u = graph[v][i];
        if (u != prev)
        {
            dp[v][1] = max(dp[v][1], (1 + dp[u][0] + dp[v][0] - max(dp[u][0], dp[u][1])));
        }
    }
    answer = max(answer, max(dp[v][0], dp[v][1]));
}
int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    dp_tree(1, -1);
    
    cout<<answer<<endl;
}