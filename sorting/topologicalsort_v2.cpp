/*
    Topological Sort v2

*/

#include <iostream>
#include <vector>
using namespace std;
const int N = 1000000 + 21;
vector<int> tab[N];
int income[N];
int ans[N];
int n, m, a, b, counter_beg = 0, counter_end = 0;
int main()
{
    cin>>n>>m;
    
    for (int i=0; i<m; i++)
    {
        cin>>a>>b;
        tab[a].push_back(b);
        income[b]++;
    }

    for (int i=1; i<=n; i++)
    {
        if (income[i] == 0)
            ans[counter_end++] = i;
    }

    while (ans[counter_beg] != 0)
    {
        int curr = ans[counter_beg];
        for (int i=0; i<tab[curr].size(); i++)
        {
            int neighbour = tab[curr][i];
            income[neighbour]--;
            if (income[neighbour] == 0)
                ans[counter_end++] = neighbour;
        }
        counter_beg++;
    }
    if (counter_beg == n)
    {
        cout<<"TRUE\n";
        for (int i=0; i<n; i++)
            cout<<ans[i]<<" ";
    }
    else
    {
        cout<<"FALSE\n";
    }

}