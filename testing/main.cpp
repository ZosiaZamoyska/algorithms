#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n, a;
vector<int> tab;
int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>a;
        tab.push_back(a);
    }

    sort(tab.begin(), tab.end());

    for (int i=0; i<n; i++)
        cout<<tab[i]<<" ";
}