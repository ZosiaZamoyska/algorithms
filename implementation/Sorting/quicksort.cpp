#include <iostream>
using namespace std;
const int N = 1e6+21;

int n;
int tab[N];

int part(int p, int q)
{
    int v = tab[q];

    int i = p-1;
    for (int j=p; j<q; j++)
    {
        if (tab[j]<v)
        {
            i++;
            swap(tab[i], tab[j]);
        }
    }
    swap(tab[i+1], tab[q]);
    return i+1;
}
void quicksort(int p, int q)
{
    if (p<q)
    {
        int curr = part(p, q);

        quicksort(p, curr-1);
        quicksort(curr+1, q);
    }
}
int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>tab[i];
    }
    quicksort(0, n-1);
    for (int i=0; i<n; i++)
    {
        cout<<tab[i]<<" ";
    }
    cout<<endl;
} 