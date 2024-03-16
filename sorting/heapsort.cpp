#include <iostream>
using namespace std;
const int N = 1e6+21;

int n;
int tab[N];
int tree[2*N];

void heap(int k, int v)
{
    int root = v;
    int l = 2*v+1, r = 2*v+2;

    if (l<k && tab[l]>tab[root])
    {
        root = l;
    }

    if (r<k && tab[r]>tab[root])
    {
        root = r;
    }

    if (root!=v)
    {
        swap(tab[v], tab[root]);
        heap(k, root);
    }
}
void heapsort()
{
    for (int i=n/2-1; i>=0; i--)
    {
        heap(n, i);
    }
    for (int i=n-1; i>=0; i--)
    {
        swap(tab[0], tab[i]);

        heap(i, 0);
    }
}

int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>tab[i];
    }

    heapsort();

    for (int i=0; i<n; i++)
    {
        cout<<tab[i]<<" ";
    }
}