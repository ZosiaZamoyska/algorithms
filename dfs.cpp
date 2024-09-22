//
//  main.cpp
//  dfs
//
//  Created by Zosia  on 28.08.2017.
//  Copyright © 2017 Zosia . All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
const int N=1000*1000+6;
vector<int> as[N];
bool vis[N];
int pre[N];
int post[N];
int x, y; // vertices, edges
int from, to;
int counter_pre=1, counter_post=1; // only if graph is a tree
void dfs(int curr)
{
    vis[curr]=true;
    
    pre[curr]=counter_pre;
    counter_pre++;
    
    for (auto &i:as[curr])
    {
        if (vis[i]==false)
        {
            dfs(i);
        }
    }
    
    post[curr]=counter_post;
    counter_post++;
    
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
    dfs(1);
    for (int i=1; i<=x; i++)
    {
        cout<<pre[i]<<" "; // pre-order
    }
    cout<<"\n";
    for (int i=1; i<=x; i++)
    {
        cout<<post[i]<<" "; // post-order
        
    }
    cout<<"\n";
}
