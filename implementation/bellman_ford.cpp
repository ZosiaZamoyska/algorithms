#include <iostream>
#include <vector>
using namespace std;
const int N = 1000+21;
const int INF = 1000000000+21;
int n, m, a, b, c;
int dist[N];
vector<pair<pair<int, int>, int> > edges;

bool bellmanFord(int v)
{
    dist[v] = 0;

    // update the distances
    for (int i=1; i<=n-1; i++)
    {
        for (int j=0; j<m; j++)
        {
            int u, v, weight;
            u = edges[j].first.first;
            v = edges[j].first.second;
            weight = edges[j].second;

            if (dist[u] != INF && dist[u] + weight < dist[v])
            {
                dist[v] = dist[u] + weight;
            }
        }
    }

    // check for negative cycles
    for (int j=0; j<m; j++)
    {
        int u, v, weight;
        u = edges[j].first.first;
        v = edges[j].first.second;
        weight = edges[j].second;

        if (dist[u] != INF && dist[u] + weight < dist[v])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    cin>>n>>m;

    for (int i=1; i<=n; i++)
        dist[i] = INF;

    for (int i=0; i<m; i++)
    {
        cin>>a>>b>>c;
        edges.push_back({{a, b}, c});
    }

    bool ans = bellmanFord(1);

    if (ans) 
    {
        for (int i=1; i<=n; i++)
        {
            if (dist[i] == INF)
                cout<<"INF ";
            else
                cout<<dist[i]<<" ";
        }
        cout<<endl;
    }
    else
    {
    	cout<<"Contains negative cycle\n";
    }
}