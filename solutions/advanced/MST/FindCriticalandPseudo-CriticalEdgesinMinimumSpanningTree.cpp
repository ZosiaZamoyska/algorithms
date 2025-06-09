/*
    Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int N = 1000+21;
vector<pair<int, pair<int, int> > > edges;
vector<int> critical;
vector<int> pseudo;
int parent[N][3];
int waga[N][3];
int n, a, b, c;
int find(int v, int i)
{
    if (parent[v][i] != v)
    {
        parent[v][i] = find(parent[v][i], i);
    }
    return parent[v][i];
}
void unite(int a, int b, int i)
{
    int par_a = find(a, i);
    int par_b = find(b, i);
    if (par_a != par_b)
    {
        if (waga[par_a] < waga[par_b])
            parent[par_a][i] = par_b;
        else {
            parent[par_b][i] = par_a;
            if (waga[par_a] == waga[par_b])
                waga[par_a][i]++;
        }
    }
}
/*int kruskal(int i)
{    
    int weight = 0;
    for (int i=0; i<edges.size(); i++)
    {
        int v = edges[i].first;
        int a = edges[i].second.first;
        int b = edges[i].second.second;

        if (find(a, i) != find(b, i))
        {
            unite(a, b, i);
            weight += v;
        }
    }
}*/
int main()
{
    cin>>n; 
    for (int i=0; i<n; i++)
    {
        cin>>a>>b>>c;
        edges.push_back({c, {a, b}});
    }
    sort(edges.begin(), edges.end());
	for (int i=0; i<=n; i++)
    {
        parent[i][0] = i;
        waga[i][0] = 1;
    }
    int weight = 0;
    for (int i=0; i<n; i++)
    {
        int v = edges[i].first;
        int a = edges[i].second.first;
        int b = edges[i].second.second;
        if (find(a, 0) != find(b, 0))
        {
            unite(a, b, 0);
            weight += v;
        }
    }


    for (int i=0; i<n; i++)
    {
        for (int i=0; i<=n; i++)
        {
            parent[i][1] = i;
            waga[i][1] = 1;
            parent[i][2] = i;
            waga[i][2] = 1;
        }

        int weight_2 = 0;
        bool is_critical = false;
        for (int j=0; j<n; j++)
        {
            if (i!=j)
            {
                int v = edges[j].first;
                int a = edges[j].second.first;
                int b = edges[j].second.second;
                if (find(a, 1) != find(b, 1))
                {
                    unite(a, b, 1);
                    weight_2 += v;
                }
            }
        }
        int v_og = edges[i].first;
        int a_og = edges[i].second.first;
        int b_og = edges[i].second.second;
        if (weight_2 > weight)
        {
            critical.push_back(i);
            is_critical = true;
        }
        
        weight_2 = 0;
        unite(a_og, b_og, 2);
        weight_2 += v_og;
        for (int j=0; j<n; j++)
        {
            int v = edges[j].first;
            int a = edges[j].second.first;
            int b = edges[j].second.second;
            if (find(a, 2) != find(b, 2))
            {
                unite(a, b, 2);
                weight_2 += v;
            }
        }
        if (weight_2 == weight && !is_critical)
        {
            pseudo.push_back(i);
        }
    }

    for (int i=0; i<critical.size(); i++)
    {
		cout<<critical[i]<<" ";
    }
	cout<<endl;
    for (int i=0; i<pseudo.size(); i++)
    {
		cout<<pseudo[i]<<" ";
    }
}
