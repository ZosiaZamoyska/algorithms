/*
    You are given an N (1 <= N <= 50), number of sticks. 
    Each stick has a length a_i (1 <= a_i <= 10^9). 
    Each stick can be split in half. The resulting sticks have to be integers.
    So, we define the lenghts of resulting sticks as floor(a_i / 2) and a_i - floor(a_i / 2).
    Whenever you split a stick, you save one and throw out the other.

    For a sequence of sticks, reply with minimum number of splitting operations required to make all sticks same length.
    For example, sticks [5, 6, 5, 6] can all become of length 3 in total of 4 operations.
*/
#include <iostream>
#include <map>
#include <vector>

using namespace std;
const int N = 50 + 5;
const int INF = 1e9+21;
int t, n;
int a[N];
map<int, int> vis;
map<int, int> cost[N];
int answer = -1;
void compute_cost(int index, int val, int curr_cost)
{
    cost[index][val] = curr_cost;
    if (val == 1)
        return;
    
    if (val%2 == 1)
    {
        if (!cost[index][(val-1)/2])
            compute_cost(index, (val-1)/2, curr_cost+1);
        if (!cost[index][(val-1)/2+1])
            compute_cost(index, (val-1)/2 + 1, curr_cost+1);
    }
    else
    {
        if (!cost[index][val/2])
            compute_cost(index, val/2, curr_cost+1);
    }
}
void find_min(int val)
{
    //cout<<val<<endl;
    vis[val] = 1;
    int total_cost = 0;
    bool possible = true;
    for (int i=0; i<n; i++)
    {
        int curr_cost = cost[i][val];
        //cout<<i<<": "<<curr_cost<<endl;
        if (curr_cost == 0)
        {
            possible = false;
        }
        total_cost += curr_cost-1;
    }
    if (possible)
    {
        //cout<<"possible: "<<" "<<total_cost<<endl;
        if (answer == -1)
            answer = total_cost;
        else
            answer = min(answer, total_cost);
    }
    if (val == 1)
        return;
    
    if (val%2 == 1)
    {
        if (!vis[(val-1)/2])
            find_min((val-1)/2);
        if (!vis[(val-1)/2+1])
            find_min((val-1)/2 + 1);
    }
    else
    {
        if (!vis[(val/2)])
            find_min(val/2);
    }
}
void clean(int val)
{
    vis[val] = 0;
    if (val%2 == 1)
    {
        if (vis[(val-1)/2])
            clean((val-1)/2);
        if (vis[(val-1)/2 + 1])
            clean((val-1)/2 + 1);
    }
    else
    {
        if (vis[val/2])
            clean(val/2);
    }
}
void cost_clean(int index, int val)
{
    cost[index][val] = 0;
    if (val == 1)
        return;
    
    if (val%2 == 1)
    {
        if (cost[index][(val-1)/2])
            cost_clean(index, (val-1)/2);
        if (cost[index][(val-1)/2+1])
            cost_clean(index, (val-1)/2 + 1);
    }
    else
    {
        if (cost[index][val/2])
            cost_clean(index, val/2);
    }
}
void solve()
{
    int min_a = a[0];
    for (int i=0; i<n; i++)
    {
        min_a = min(min_a, a[i]);
        compute_cost(i, a[i], 1);
    }
    
    find_min(min_a);
    clean(min_a);
    for (int i=0; i<n; i++)
        cost_clean(i, a[i]);
}
int main()
{
    cin>>t;
    while (t--)
    {
        cin>>n;
        for (int i=0; i<n; i++)
            cin>>a[i];
        
        
        solve();
        cout<<answer<<endl;
        answer = -1;
        for (int i=0; i<n; i++)
            a[i] = 0;
    }
    
}