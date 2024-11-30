/*
    Check if given graph is a valid tree (Find and Union)
*/

#include <iostream>
#include <vector>
using namespace std;
const int N = 100000+21;
vector<int> graph[N];
int vis[N];
int n, m, a, b;

bool dfs(int v, int prev)
{
    if (vis[v])
        return false;
    bool ans = true;
    vis[v] = 1;
    for (int i=0; i<graph[v].size(); i++)
    {
        int curr = graph[v][i];
        if (curr != prev && dfs(curr, v)==false)
            ans = false;
    }
    return ans;
}

int main()
{
	cin>>n>>m;
    if (m == n-1)
    {
    	for (int i=0; i<m; i++)
        {
            cin>>a>>b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        bool odp = dfs(0, -1);
        if (odp)
        {
            cout<<"TRUE\n";
        }
        else
        {
            cout<<"FALSE\n";
        }
        }
    else
    {
        for (int i=0; i<m; i++)
        {
            cin>>a>>b;
        }
        cout<<"FALSE\n";
    }
}
