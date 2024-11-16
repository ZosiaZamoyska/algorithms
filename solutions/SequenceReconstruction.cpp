/*

    Sequence Reconstruction

*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int N = 100000+21;
int n, m, k, a, b=-1;
vector<int> org;
vector<int> graph[N];
queue<int> Q;
int income[N];
bool topologicalsort()
{
    int index = 0;
    while (!Q.empty())
    {
        if (Q.size() > 1)
        {
            return false;
        }
        int curr = Q.front();
        Q.pop();

        if (curr != org[index])
        
            return false;
        index++;
        for (int i=0; i<graph[curr].size(); i++)
        {
            int neighbour = graph[curr][i];
            income[neighbour]--;
            if (income[neighbour] == 0)
                Q.push(neighbour);
        }
    }
    return true;
}
int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>a;
        org.push_back(a);
    }

    cin>>m;
    for (int i=0; i<m; i++)
    {
        b = -1;
        cin>>k;
        for (int j=0; j<k; j++)
        {
            cin>>a;
            if (b != -1)
            {
                graph[b].push_back(a);
                income[a]++;
            }
            b = a;
        }
    }

    for (int i=1; i<=n; i++)
    {
        if (income[i] == 0)
            Q.push(i);
    }
    bool ans = topologicalsort();
    if (ans)
    	cout<<"TRUE\n";
    else
    	cout<<"FALSE\n";
}