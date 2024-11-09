/*
    Rich and Loud

*/

#include <iostream>
#include <vector>
using namespace std;
const int N = 500;
vector<int> tab[N];
int cichy[N];
int vis[N];
int ans[N];
int n, m, a, b;
void dfs(int v)
{
    if (ans[v] != -1)
        return;
    
    ans[v] = v;
    for (int i=0; i<tab[v].size(); i++)
    {
        int neighbour = tab[v][i];
        dfs(neighbour);
        if (cichy[ans[neighbour]] < cichy[ans[v]])
            ans[v] = ans[neighbour];
    }
}

int main()
{
    cin>>n>>m;

    for (int i=0; i<m; i++)
    {
        cin>>a>>b;
        tab[b].push_back(a);
    }
    for (int i=0; i<n; i++)
    {
        cin>>cichy[i];
    	ans[i] = -1;
    	
    }    
    for (int i=0; i<n; i++)
    {
        dfs(i);
    }
    for (int i=0; i<n; i++)
        cout<<ans[i]<<" ";
}