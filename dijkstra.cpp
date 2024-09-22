//
//  main.cpp
//  dijkstra
//
//  Created by Zosia  on 28.08.2017.
//  Copyright © 2017 Zosia . All rights reserved.
//

#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int N=1000*1000+6;
const int INF=1000*1000*1000+33;
struct edge
{
    int dest;
    int dist;
};
vector<edge> as[N]; // graph 
int dis[N];
int x, y; // vertices, edges;
int from, to, dist;
void dijkstra(int a)
{
    for (int i=1; i<=x; i++)
    {
        dis[i]=INF;
    }
    priority_queue<pair<int, int> > Q; // current verticle, distance
    Q.push(make_pair(0, a));
    dis[a]=0;
    while (!Q.empty())
    {
        pair<int, int> curr=Q.top();
        Q.pop();
        for (auto &i:as[curr.second])
        {
            if (dis[i.dest]>dis[curr.second]+i.dist)
            {
                dis[i.dest]=dis[curr.second]+i.dist;
                Q.push(make_pair(-(dis[i.dest]), i.dest));
            }
        }
    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin>>x>>y;
    for (int i=0; i<y; i++)
    {
        cin>>from>>to>>dist;
        as[from].push_back({to, dist});
        as[to].push_back({from, dist});
    }
    dijkstra(1); 
    // distance from vertex 1 
    for (int i=1; i<=x; i++)
    {
        cout<<dis[i]<<" ";
    }
}
