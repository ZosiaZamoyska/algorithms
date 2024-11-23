/*
    Evaluate Division

    given a series of proportions between variables, evaluate proportions between other pairs if possible
*/

#include <iostream>
#include <vector>
#include <map>
using namespace std;
const int N = 21;
vector<char> eq[2];
vector<double> val;
map<char, double> waga;
map<char, char> parent;
int n, m;
double value;
char var_a, var_b;

char find(char x){
    if (parent[x] != x)
    {
        char og_par = parent[x];
        parent[x] = find(parent[x]);
        waga[x] *= waga[og_par];
    }
    return parent[x];
}

int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>var_a>>var_b>>value;
        eq[0].push_back(var_a);
        eq[1].push_back(var_b);
        val.push_back(value);
        parent[var_a] = var_a;
        parent[var_b] = var_b;
        waga[var_a] = 1.0;
        waga[var_b] = 1.0;
    }
    for (int i=0; i<n; i++)
    {
        char var_a = eq[i][0];
        char var_b = eq[i][1];
        char par_a = find(var_a);
        char par_b = find(var_b);

        if (par_a == par_b)
            continue;
        parent[par_a] = par_b;
        waga[par_a] = waga[par_b] * val[i] / waga[par_a];
    }

    cin>>m;
    for (int i=0; i<m; i++)
    {
        cin>>var_a>>var_b;
        if (find(var_a) == find(var_b))
        {
            cout<<waga[var_a]/waga[var_b]<<endl; 
        }
        else
        {
            cout<<"no\n";
        }
    }


}