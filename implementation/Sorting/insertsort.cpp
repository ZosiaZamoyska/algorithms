#include <iostream>
using namespace std;
const int N = 1e6+21;

int n;
int tab[N];

void insertsort()
{
    for (int i=1; i<n; i++)
    {
        int val = tab[i];
        int k = i-1;

        while (k>=0 && tab[k]>val)
        {
            tab[k+1] = tab[k];
            k--;
        }
        tab[k+1] = val;
    }
}
int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>tab[i];
    }
    insertsort();
    for (int i=0; i<n; i++)
    {
        cout<<tab[i]<<" ";
    }
}