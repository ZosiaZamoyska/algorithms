/*
    Fibonacci with memorization
*/ 

#include <iostream>
using namespace std;
const int N = 1000;
int n;
int tab[N];
int fib(int a)
{
    if (a<=2)
        return 1;
    
    if (!tab[a])
        if (!tab[a-1])
            tab[a-1] = fib(a-1);
        if (!tab[a-2])
            tab[a-2] = fib(a-2);
        tab[a] = tab[a-1] + tab[a-2];

    return tab[a];
}
int main()
{
    cin>>n;
    cout<<fib(n)<<endl;
}