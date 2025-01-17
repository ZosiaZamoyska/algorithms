//
// binary tree (for finding max)
// by Zosia @ 2024/09/22
//

#include <iostream>
using namespace std;
const int N = 1e6 + 21;
int n, base = 1;
int tab[N];
int tree[2*N];

void build_tree() // building tree, run once - O(n)
{
    for (int i=0; i<n; i++)
    {
        tree[i+base] = tab[i];
    }
    for (int i=n-1; i>0; i--)
    {
        tree[i] = max(tree[2*i], tree[2*i+1]);
    }
}

void change_value(int k, int v) // changing element value at position k to v - O(log(n))
{
    tree[k+base] = v;
    int index = (k+base)/2;
    while (index >= 1)
    {
        tree[index] = max(tree[2*index], tree[2*index+1]);
        index /= 2;
    }
}

int find_max()
{
    return tree[1];
}

void display_tree()
{
    int power = 2;
    for (int i=1; i<2*n; i++)
    {
        if (power == i)
        {
            cout<<endl;
            power *= 2;
        }
        cout<<tree[i]<<" ";
       
    }
    cout<<endl;
}

int main()
{
    // input 
    cin>>n;
    for (int i=0; i<n; i++)
        cin>>tab[i];

    // finding base
    while (base < n)
        base *= 2;

    build_tree();
    display_tree();
    change_value(1, 1);
    display_tree();
    cout<<find_max()<<endl;
}