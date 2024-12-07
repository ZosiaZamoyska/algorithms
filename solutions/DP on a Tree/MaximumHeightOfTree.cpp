/*
    Maximum Height of tree when any node can be a root

*/

#include <iostream>
#include <vector>
using namespace std;
const int N = 500000+21;
vector<int> graph[N];
int in[N];
int out[N];
int n, a, b;
int dfs_in(int v, int p)
{
    int ans = 0;
    for (int i=0; i<graph[v].size(); i++)
    {
        int neighbour = graph[v][i];
        if (neighbour != p)
            ans = max(ans, dfs_in(neighbour, v) + 1);
    }
    return in[v] = ans;
}
void dfs_out(int v, int p)
{
    int ans1 = 0, ans2 = 0;
    for (int i=0; i<graph[v].size(); i++)
    {
        int neighbour = graph[v][i];
        if (neighbour != p)
        {
            if (in[neighbour] >= ans1)
            {
                ans2 = ans1; 
                ans1 = in[neighbour];
            }
            else if (in[neighbour] >= ans2)
                ans2 = in[neighbour];
        }
    }
    for (int i=0; i<graph[v].size(); i++)
    {
        int neighbour = graph[v][i];
        if (neighbour != p)
        {
            int ans = ans1;
            if (in[neighbour] == ans1)
                ans = ans2;

            out[neighbour] = max(out[v], ans + 1) + 1;
            dfs_out(neighbour, v);
        }
    }
}
int main()
{
    cin>>n;
    for (int i=1; i<n; i++)
    {
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    dfs_in(1, -1);

    dfs_out(1, -1);


    int answer = 0;
    for (int i=1; i<=n; i++)
        answer = max(answer, max(in[i], out[i]));
     
    cout<<answer<<endl;
}