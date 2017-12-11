//
//  main.cpp
//  przedzialy
//
//  Created by Złosia  on 10.12.2017.
//  Copyright © 2017 Złosia . All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int N=200*1000+21;
struct prze{
    int pocz;
    int kon;
};
bool cmp(prze a, prze b)
{
    if (a.kon==b.kon)
        return a.pocz<b.pocz;
    else
        return a.kon<b.kon;
}
int x, a, b;
int zli, koniec=-1;
vector<prze> as;
prze tmp;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin>>x;
    for (int i=0; i<x; i++)
    {
        cin>>a>>b;
        tmp.pocz=a, tmp.kon=b;
        as.push_back(tmp);
    }
    sort(as.begin(), as.end(), cmp);
    for (int i=0; i<x; i++)
    {
        if (as[i].pocz>=koniec)
        {
            koniec=as[i].kon;
            zli++;
        }
    }
    cout<<zli<<endl;
    return 0;
}
