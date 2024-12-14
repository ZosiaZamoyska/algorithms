/*
    Find a peak in an array

    Example
    6, 8, 9, 14, 10, 12 
*/

#include <iostream>
using namespace std; 
const int N = 500000+21;
int tab[N];
int n;
int findPeak(int left, int right)
{
    if (left == right)
        return tab[left];
    int mid = (left+right)/2;

    int peak1 = findPeak(left, mid);
    int peak2 = findPeak(mid+1, right);
    return max(peak1, peak2);
}
int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
        cin>>tab[i];
    cout<<findPeak(0, n-1);
}