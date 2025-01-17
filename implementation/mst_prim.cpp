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
0 1 4
0 7 8
7 6 1
6 5 2
5 2 4
2 8 2
2 3 7
3 4 9
*/