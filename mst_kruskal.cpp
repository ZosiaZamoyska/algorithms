/* 
    MST with Kruskal's algorithm
*/
#include <iostream>
#include <vector>
using namespace std;
const int N = 100000+21;
vector<pair<int, int> > graph[N];
int n, m, a, b, c;
int main()
{
    cin>>n>>m;
    for (int i=0; i<n; i++)
    {
        cin>>a>>b>>c;
        graph[a].push_back(make_pair(b, c));
        graph[b].push_back(make_pair(a, c));
    }

    
}