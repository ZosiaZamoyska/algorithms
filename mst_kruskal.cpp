/* 
    MST with Kruskal's algorithm
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int N = 100000+21;
vector<pair<int, pair<int, int> > > edges;
vector<pair<pair<int, int>, int> > ans;
int parent[N];
int waga[N];
int n, m, a, b, c;
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
int main()
{
    cin>>n>>m;
    for (int i=0; i<n; i++)
    {
        cin>>a>>b>>c;
        edges.push_back({c, {a, b}});
    }
    for (int i=0; i<=n; i++)
    {
        parent[i] = i;
        waga[i] = 1;
    }

    sort(edges.begin(), edges.end());

    kruskal();

    for (int i=0; i<ans.size(); i++)
    {
        cout<<ans[i].first.first<<" "<<ans[i].first.second<<" "<<ans[i].second<<endl;
    }
}

/*
Example:
9 14
0 1 4
0 7 8
1 2 8
1 7 11
2 3 7
2 8 2
2 5 4
3 4 9
3 5 14
4 5 10
5 6 2
6 7 1
6 8 6
7 8 7

Answer:
2 8 2
0 1 4
2 5 4
2 3 7
0 7 8
1 2 8
3 4 9
*/