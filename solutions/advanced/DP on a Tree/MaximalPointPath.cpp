/*
    Maximal Point Path

*/ 
#include <iostream>
#include <vector>
using namespace std;
const int N = 500000+21;
vector<pair<int, int> > graph[N];
int dp[N];
int vis[N];
int points[N];
int n, a, b, c;
int ans;
void dfs(int v)
{
    vis[v] = 1;
    int ans1 = 0, ans2 = 0;
    for (int i=0; i<graph[v].size(); i++)
    {
        int curr = graph[v][i].first;
        int weight = graph[v][i].second;

        if (!vis[curr])
        {
            dfs(curr);
        }
        int cost = dp[curr] - weight;

        if (cost >= ans1)
        {
            ans2 = ans1;
            ans1 = cost;
        }
        else if (cost >= ans2)
            ans2 = cost;
    }
    ans = max(ans, ans1 + ans2 + points[v]);

    dp[v] = ans1 + points[v];
}
int main()
{
    cin>>n;
    for (int i=1; i<=n; i++)
        cin>>points[i];
    
    for (int i=1; i<n; i++)
    {
        cin>>a>>b>>c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }

    dfs(1);
    
    cout<<ans<<endl;
}