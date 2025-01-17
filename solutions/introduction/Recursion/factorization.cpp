/*
    Factorization
*/

#include <iostream>
using namespace std;
int n;
int fact(int a)
{
    if (a<=1)
        return 1;

    return a*fact(a-1);
}
int main()
{
    cin>>n;
    cout<<fact(n)<<endl;
}