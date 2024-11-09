/*
    Minimum Height Trees

    Take a Tree and find node to make the height of tree minimum.

*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int N = 1000*1000+21;
vector<int> tab[N];
int income[N];
int n, m, a, b;
queue<int> Q;
vector<int> ans;
int main()
{
    cin>>n>>m;

    for (int i=0; i<m; i++)
    {
        cin>>a>>b;
        tab[a].push_back(b);
        tab[b].push_back(a);
        income[a]++;
        income[b]++;
    }

    for (int i=1; i<=n; i++)
        if (income[i] == 1)
            Q.push(i);

    while (!Q.empty())
    {
        ans.clear();

        int curr_level = Q.size();
        for (int i=0; i<curr_level; i++)
        {
            int curr = Q.front();
            Q.pop();
            ans.push_back(curr);
            for (int j=0; j<tab[curr].size(); j++)
            {
                int neighbour = tab[curr][j];
                income[neighbour]--;
                if (income[neighbour] == 1)
                    Q.push(neighbour);
            }
        }
    }
    for (int i=0; i<ans.size(); i++)
    	cout<<ans[i]<<" ";
}