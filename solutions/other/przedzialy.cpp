/*
    For given n compartments, their start and end, print out how many (at most) non-overlapping compartments can we chose.

    5
    5 6
    1 4
    10 10
    6 9
    8 10

    Answer is 4
*/

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
