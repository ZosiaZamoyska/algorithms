//
// Two Pointer Technique (for finding a sequence summing to X)
// by Zosia @ 2024/09/22
//


#include <iostream>
using namespace std;
const int N = 1e6 + 21;
int n, k;
int tab[N];

bool twopointer()
{
    bool ans = false;

    int j = 0;
    int sum = tab[0];
    for (int i=0; i<n; i++)
    {
        while (sum < k && j < n)
        {
            j++;
            sum += tab[j];
        }
        if (sum == k)
            ans = true;
        
        sum -= tab[i];
    }

    return ans;
}

int main()
{
    // input 
    cin>>n>>k; 
    for (int i=0; i<n; i++)
        cin>>tab[i];

    if (twopointer())
    	cout<<"There exists a consecutive sequence summing up to "<<k<<endl;
}