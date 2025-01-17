/*
    Longest Consecutive Sequence

    Given an array of numbers, return longest consecutive sequence length (any order of elements in array)
*/
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;
const int N = 100000+21;
vector<int> tab;
unordered_set<int> S;
int n, a;
int main()
{
	cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>a;
        tab.push_back(a);
    }
    unordered_set<int> S(tab.begin(), tab.end());
    
    int odp = 0;
    
    for (int i=0; i<n; i++)
    {
        int curr = tab[i];
        if (!S.count(curr-1))
        {
        while (S.count(curr))
                    curr++;
        odp = max(odp, curr - tab[i]);
        }
    }
    cout<<odp<<endl;
}