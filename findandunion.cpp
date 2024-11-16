#include <iostream>
using namespace std;
const int N = 100000+21;
int parent[N];
int sizing[N];
int n, a, b;
int find1(int i)
{
    if (parent[i] == i)
        return i;
    else
        return find1(parent[i]);
}

int find2(int i)
{
    if (parent[i] == i)
        return i;
    else
    {
        int result = find2(parent[i]);
        parent[i] = result;
        return result;
    }
}

void union1(int i, int j)
{
    int i_par = find1(i);
    int j_par = find1(j);

    parent[i] = j;
}

void union2(int i, int j)
{
    int i_par = find2(i);
    int j_par = find2(j);
    if (i_par == j_par)
        return;
    if (sizing[i_par] < sizing[j_par])
    {
        parent[i_par] = j_par;
        sizing[j_par] += sizing[i_par];
    }
    else
    {
        parent[j_par] = i_par;
        sizing[i_par] += sizing[j_par];
    }
    
}

int main()
{
    cin>>n;
    for (int i=0; i<=n; i++)
        parent[i] = i;
    for (int i=0; i<n; i++)
    {
        cin>>a>>b;
        union2(a, b);
    }
}