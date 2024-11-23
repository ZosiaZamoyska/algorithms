/*
    Min Cost to Connect All Points

    MST, but you're given (xi, yi) points
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int N = 1000+21;
vector<pair<int, int> > graph[N];
vector<pair<int, pair<int, int> > > edges;
vector<pair<pair<int, int>, int> > ans;
int point[N][2];
int vis[N];
int edge[N];
int n, x, y;
int parent[N];
int waga[N];
int find(int v)
{
    if (parent[v] != v)
    {
        parent[v] = find(parent[v]);
    }
    return parent[v];
}
void unite(int a, int b)
{
    int par_a = find(a);
    int par_b = find(b);
    if (par_a != par_b)
    {
        if (waga[par_a] < waga[par_b])
            parent[par_a] = par_b;
        else {
            parent[par_b] = par_a;
            if (waga[par_a] == waga[par_b])
                waga[par_a]++;
        }
    }
}
void kruskal()
{
    for (int i=0; i<edges.size(); i++)
    {
        int v = edges[i].first;
        int a = edges[i].second.first;
        int b = edges[i].second.second;

        if (find(a) != find(b))
        {
            unite(a, b);
            ans.push_back({{a, b}, v});
        }
    }
}
void prim()
{
    int start = 0; 
    priority_queue<pair<int, pair<int, int> > > Q;

    Q.push({0, {start, start}});

    while (!Q.empty())
    {
        pair<int, pair<int, int> > curr = Q.top();
        int curr_v = curr.second.first;
        Q.pop();

        if (vis[curr_v])
            continue;
        vis[curr_v] = true;
        if (curr.second.second != curr.second.first)
            ans.push_back({{curr.second.second, curr.second.first}, -curr.first});

        for (int i=0; i<graph[curr_v].size(); i++)
        {
            int v = graph[curr_v][i].first;
            int waga = graph[curr_v][i].second;
            if (vis[v] != true)
            {
                Q.push({-waga, {v, curr_v}});
            }
        }
    }
}
int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>point[i][0]>>point[i][1];
    }

    for (int i=0; i<=n; i++)
    {
        parent[i] = i;
        waga[i] = 1;
    }

    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
        {
            int x0 = point[i][0];
            int x1 = point[j][0];
            int y0 = point[i][1];
            int y1 = point[j][1];
            if (i!=j)
            {
                int dist = abs(x0 - x1) + abs(y0 - y1);
                // i -> j, dist
                edges.push_back({dist, {i, j}});
                graph[i].push_back({j, dist});
                graph[j].push_back({i, dist});
            }
        }
    }

    prim();

    for (int i=0; i<ans.size(); i++)
    {
        cout<<ans[i].first.first<<" "<<ans[i].first.second<<" "<<ans[i].second<<endl;
    }
}