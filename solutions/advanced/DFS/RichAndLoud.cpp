/*
    Rich and Loud

    You are given an array richer where richer[i] = [ai, bi] indicates that ai has more money than bi and an integer array quiet where quiet[i] is the quietness of the ith person. All the given data in richer are logically correct (i.e., the data will not lead you to a situation where x is richer than y and y is richer than x at the same time).

    Return an integer array answer where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]) among all people who definitely have equal to or more money than the person x.
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