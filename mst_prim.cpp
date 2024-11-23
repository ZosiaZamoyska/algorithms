/* 
    MST with Prim's algorithm
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int N = 100000+21;
vector<pair<int, int> > graph[N];
int n, m, a, b, c;
int vis[N];
int edge[N];
vector<pair<int, int> > ans;
void prim()
{
    int start = 0; 
    priority_queue<pair<int, int> > Q;

    Q.push({0, start});

    while (!Q.empty())
    {
        pair<int, int> curr = Q.top();
        int curr_v = curr.second;
        Q.pop();

        if (vis[curr_v])
            continue;
        vis[curr_v] = true;
        ans.push_back({curr_v, -curr.first});

        for (int i=0; i<graph[curr_v].size(); i++)
        {
            int v = graph[curr_v][i].first;
            int waga = graph[curr_v][i].second;
            if (vis[v] != true)
            {
                Q.push({-waga, v});
            }
        }
    }
}

int main()
{
    cin>>n>>m;
    for (int i=0; i<n; i++)
    {
        cin>>a>>b>>c;
        graph[a].push_back(make_pair(b, c));
        graph[b].push_back(make_pair(a, c));
    }

    prim();

    for (int i=0; i<ans.size(); i++)
    {
        cout<<ans[i].first<<" "<<ans[i].second<<endl;
    }
}