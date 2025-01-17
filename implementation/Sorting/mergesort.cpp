#include <iostream>
using namespace std;
const int N = 1e6+21;

int n;
int tab[N];

void merge(int p, int m, int q)
{
    int a1 = m-p+1;
    int a2 = q-m;

    int L[a1], R[a2];

    for (int i=0; i<a1; i++)
    {
        L[i] = tab[p+i];
    }
    for (int i=0; i<a2; i++)
    {
        R[i] = tab[m+1+i];
    }

    int i=0, j=0, k=p;

    while (i<a1 && j<a2)
    {
        if (L[i]<=R[j])
        {
            tab[k] = L[i];
            i++;
        }
        else
        {
            tab[k] = R[j];
            j++;
        }
        k++;
    }
    while (i<a1)
    {
        tab[k] = L[i];
        i++;
        k++;
    }
    while (j<a2)
    {
        tab[k] = R[j];
        j++;
        k++;
    }
}

void mergesort(int p, int q)
{
    if (p<q)
    {
        int m = (p+q-1)/2;
        mergesort(p, m);
        mergesort(m+1, q);
        merge(p, m, q);
    }
}

int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>tab[i];
    }

    mergesort(0, n-1);

    for (int i=0; i<n; i++)
    {
        cout<<tab[i]<<" ";
    }
}