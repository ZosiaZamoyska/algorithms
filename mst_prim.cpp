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
vector<pair<pair<int, int>, int> > ans;
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
    cin>>n>>m;
    for (int i=0; i<m; i++)
    {
        cin>>a>>b>>c;
        graph[a].push_back(make_pair(b, c));
        graph[b].push_back(make_pair(a, c));
    }

    prim();

    for (int i=0; i<ans.size(); i++)
    {
        cout<<ans[i].first.first<<" "<<ans[i].first.second<<" "<<ans[i].second<<endl;
    }
}