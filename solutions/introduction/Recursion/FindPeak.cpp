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
        return left;
    int mid = (left+right)/2;

    if (tab[mid] > tab[mid-1] && tab[mid] > tab[mid+1])
        return mid;
    else if (tab[mid] < tab[mid+1])
        return findPeak(mid+1, right);
    else return findPeak(left, mid-1);
}
int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
        cin>>tab[i];
    cout<<findPeak(1, n-2);
}