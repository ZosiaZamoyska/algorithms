// Priority Queue
// Binary Heap

#include <iostream>
using namespace std;
const int N = 1e6+21;
int n, m, a, b, size_n = 0;
int val[N];
int tree[N];

void insert(int v)
{
    size_n++;
    tree[size_n] = v;
    int k = size_n;
    while (k>1 && tree[k] > tree[k/2])
    {
        swap(tree[k], tree[k/2]);
        k/=2;
    }
}

int max_heap()
{
    return tree[1];
}

void restore(int node)
{
    int left = 2*node;
    int right = 2*node + 1;
    int maxi = node;
    if (left <= size_n && tree[left] > tree[maxi])
    {
        maxi = left;
    }
    if (right <= size_n && tree[right] > tree[maxi])
    {
        maxi = right;
    }
    if (maxi > node)
    {
        swap(tree[node], tree[maxi]);
        restore(maxi);
    }
}

void delete_max()
{
    tree[1] = tree[size_n];
    size_n--;
    restore(1);
}

void input()
{
    cin>>n;
    for (int i=1; i<=n; i++)
    {
        cin>>a;
        tree[i] = a;
    }
    size_n = n;
    for (int i=n/2; i>=1; i--)
        restore(i);
}
void operations()
{
    cin>>m;
    for (int i=0; i<m; i++)
    {
        cin>>a;
        if (a==0)
        {
            cout<<max_heap()<<endl;
        }
        if (a==1)
        {
            delete_max();
        }
        if (a==2)
        {
            cin>>b;
            insert(b);
        }
    }
}

void print_heap()
{
    for (int i=1; i<=size_n; i++)
    {
        cout<<tree[i]<<" ";
    }
    cout<<endl;
}
int main()
{
    // input takes n (node count) and n node values
    input();
    print_heap();
    // operations takes m (operation count) and m lines formatted as following:
    // (operation type, optional: operation parameters)
    // MAX: (0) - returns max value in the heap
    // DELETE MAX: (1) - deletes max value in the heap
    // ADD NODE: (2, v) - adds a node with value v to the heap
    operations();
    print_heap();
}