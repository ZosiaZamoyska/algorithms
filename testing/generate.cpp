#include <iostream>
#include <stdlib.h>
using namespace std;
const int N = 1000000+21;
int n;
int main()
{
    srand (time(NULL));

    n = rand() % N;
    for (int i=0; i<n; i++)
    {
        cout<<i<<" ";
    }
}