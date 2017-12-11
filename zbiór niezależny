#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int N=200*1000+21;
vector<int> as[N];
int tab1[N]; // bierzemy i
int tab2[N]; // nie bierzemy i
bool odw[N];
void oblicz(int a)
{
    int wyn1=0, wyn2=0;
    odw[a]=true;
    for (int i=0; i<as[a].size(); i++)
    {
        if (odw[as[a][i]]==false)
            oblicz(as[a][i]);
        // jesli bierzemy, to bierzemy niebrane od dzieci
        wyn1+=tab2[as[a][i]];
        // jesli nie bierzemy to maximum
        wyn2+=max(tab1[as[a][i]], tab2[as[a][i]]);
    }
    tab1[a]=wyn1+1;
    tab2[a]=wyn2;
}
int main()
{
    ios_base::sync_with_stdio(0);
    int x, a, b;
    cin>>x;
    for (int i=1; i<x; i++)
    {
        cin>>a>>b;
        as[a].push_back(b);
        as[b].push_back(a);
    }
    oblicz(1);
    cout<<max(tab1[1], tab2[1])<<endl;
}
