//
//  main.cpp
//  bfs
//
//  Created by Złosia  on 28.08.2017.
//  Copyright © 2017 Złosia . All rights reserved.
//

#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int N=1000*1000+6;
const int INF=1000*1000*1000+33;
vector<int> as[N];
int dis[N];
int x, y; // vertices, edges;
int from, to;
void bfs(int a)
{
    for (int i=1; i<=x; i++)
    {
        dis[i]=INF;
    }
    queue<int> Q;
    Q.push(a);
    dis[a]=0;
    while (!Q.empty())
    {
        int curr=Q.front();
        Q.pop();
        for (auto &i:as[curr])
        {
            if (dis[i]>dis[curr]+1)
            {
                dis[i]=dis[curr]+1;
                Q.push(i);
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
        cin>>from>>to;
        as[from].push_back(to);
        as[to].push_back(from);
    }
    bfs(1);
    for (int i=1; i<=x; i++)
    {
        cout<<dis[i]<<" ";
    }
}
