//
//  main.cpp
//  hurt
//
//  Created by Złosia  on 22.10.2017.
//  Copyright © 2017 Złosia . All rights reserved.
//

#include <iostream>
#include <set>
using namespace std;
const int N=1000*1000+21;
struct wie
{
    int war;
    int ind;
};
int x, wyn;
int tab1[N];
wie tab2[N];
multiset<pair<int, int> > as;
multiset<int> lista;
int main()
{
    ios_base::sync_with_stdio(0);
    cin>>x;
    for (int i=0; i<x; i++)
    {
        cin>>tab1[i];
        
    }
    for (int i=0; i<x; i++)
    {
        cin>>tab2[i].war;
        tab2[i].ind=i;
    }
    unsigned long long int curr=0;
    for (int i=0; i<x; i++)
    {
        curr+=tab1[i];
        if (curr>=tab2[i].war)
        {
            // spełniamy
            curr-=tab2[i].war;
            as.insert(make_pair(-tab2[i].war, i));
            wyn++;
        }
        else
        {
            multiset<pair<int, int> >::iterator k=as.begin();
            int val=(*k).first;
            if ((-val)>tab2[i].war)
            {
                as.erase(as.begin());
                curr-=val;
                curr-=tab2[i].war;
                as.insert(make_pair(-tab2[i].war, i));
            }
        }
    }
   cout<<as.size()<<endl;
    /*for (multiset<pair<int, int> >::iterator i=as.begin(); i!=as.end(); ++i)
    {
        lista.insert((*i).second+1);
    }
    for (multiset<int>::iterator i=lista.begin(); i!=lista.end(); ++i)
    {
        cout<<*i<<" ";
    }*/
    return 0;
}
