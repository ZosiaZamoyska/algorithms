/*
    All Paths from Source Lead to Destination

    Given graph, source, and destination - check if all paths lead to destination. 
*/

#include <iostream>
#include <vector>
using namespace std;
const int N = 1000*1000+21;
vector<int> tab[N];
int vis[N];
int flag[N];
int n, m, s, d, a, b;

bool dfs(int v)
{
    if (flag[v] != 0)
        return flag[v] == 1;

    if (v == d)
        return tab[v].size() == 0;

    if (tab[v].size() == 0) 
        return false;
        
    if (vis[v] == 1)
    	return false;
    
    vis[v] = 1;

    for (int i=0; i<tab[v].size(); i++)
    {
        int curr = tab[v][i];
        
    	bool k = dfs(curr);
        if (!k)
        {
        	flag[curr] = -1;
            return false;
        }
    }
    flag[v] = 1;
    vis[v] = 0;
    return true;
}

int main()
{
    cin>>n>>m;
    cin>>s>>d;
    for (int i=0; i<n; i++)
    {
        cin>>a>>b;
        tab[a].push_back(b);
        //tab[b].push_back(a);
    }

    if (dfs(s))
        cout<<"TRUE\n";
    else
        cout<<"FALSE\n";

}