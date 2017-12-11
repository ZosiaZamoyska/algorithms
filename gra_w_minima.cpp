//
//  main.cpp
//  gra w minima
//
//  Created by Złosia  on 10.12.2017.
//  Copyright © 2017 Złosia . All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int N=1000*1000+21;
long long int odp[N];
vector<long long int> as;
int x, a;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin>>x;
    for (int i=0; i<x; i++)
    {
        cin>>a;
        as.push_back(a);
    }
    sort(as.begin(), as.end());
    odp[0]=as[0];
    for (int i=1; i<x; i++)
    {
        odp[i]=max(as[i]-odp[i-1], odp[i-1]);
    }
    cout<<odp[x-1]<<"\n";
    return 0;
}
