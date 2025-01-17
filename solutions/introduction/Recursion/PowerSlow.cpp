/*
    Power of x to n, slow
*/
#include <iostream>
using namespace std;
int x, n;
int power(int a, int b)
{
    if (a == 0)
        return 0;
    if (b == 0)
        return 1;
    return a * power(a, b-1);
}
int main()
{
    cin>>x>>n;
    cout<<power(x, n)<<endl;
}