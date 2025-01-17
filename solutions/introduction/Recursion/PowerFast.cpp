/*
    Power of x to n, fast
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
    int curr = power(a, b/2);
    if (b%2)
        return a*curr*curr;
    else
        return curr*curr;
}
int main()
{
    cin>>x>>n;
    cout<<power(x, n)<<endl;
}