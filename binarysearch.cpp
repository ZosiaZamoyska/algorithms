//
//  main.cpp
//  binary search
//
//  Created by Złosia  on 28.08.2017.
//  Copyright © 2017 Złosia . All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;
const int N=1000*1000+6;
int arr[N];
int x, y; // number of elements, query
bool fnct(int current, int query)
{
    if (current>=query)
    {
        return true;
    }
    else
        return false;
}
int bs(int first, int last, int query)
{
    int mid;
    while (first<last) // or last-first>1 && return last in some situations
    {
        mid=(first+last)/2;
        if (fnct(arr[mid], query)==true)
        {
            last=mid;
        }
        else
        {
            first=mid+1;
        }
    }
    return first;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin>>x;
    for (int i=0; i<x; i++)
    {
        cin>>arr[i];
    }
    sort(arr, arr+x);
    cin>>y;
    int answer=bs(0, x-1, y);
    cout<<answer<<"\n";
    return 0;
}
