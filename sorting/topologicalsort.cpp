//
//  main.cpp
//  dijkstra
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
int incom[N];
int order[N];
int counter_beg=1, counter_end=1;
int x, y; // vertices, edges
int from, to;
int main()
{
    ios_base::sync_with_stdio(0);
    cin>>x>>y;
    
    // I keep my graph in vector<int> as, but I'm deleting elements of it while sorting
    // so it's good to keep your graph in another vector<int>
    
    for (int i=0; i<y; i++)
    {
        cin>>from>>to;
        as[from].push_back(to);
        incom[to]++;
    }
    for (int i=1; i<=x; i++)
    {
        if (incom[i]==0) // if there is no incoming edges, this vertex is on the topp
        {
            order[counter_end++]=i;
        }
    }
    for (int i=1; i<=x; i++)
    {
        int curr=order[counter_beg];
        counter_beg++;
        while (!as[curr].empty())
        {
            // I'm deleting vertex by subtracting edges between current vertex and its sons
            // I need to decrease number of incoming edges to current vertex sons
            incom[as[curr].back()]--;
            // if current vertex son is at the top (because the edge between current vertex and its son was the last thing incoming to the current vertex son) we put next on our topological sorted array
            if (incom[as[curr].back()]==0)
            {
                order[counter_end++]=as[curr].back();
            }
            // and so we delete the edge
            as[curr].pop_back();
        }
    }
    for (int i=1; i<=x; i++)
    {
        cout<<order[i]<<" ";
    }
}
