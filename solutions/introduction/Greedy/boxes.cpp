/*

    You are given a sequence of n distinct integers from 1 to n, stored inside n boxes. 
    There is one additional empty box labeled n+1.
    At any time, you are allowed to swap the content of the empty box with any other box.

    Your goal is to sort the boxes so that box i contains the integer i for all 1 ≤ i ≤ n. 
    Determine some, true number of swap operations needed using the empty box, and print the sequence of positions you used to swap with the empty box (including the final swap that places n+1 back in position n+1).
    If the number of operations exceeds 1500, do not output anything.

    Input:
    1
    3
    2 3 1

    Output:
    4
    2 1 3 4
*/
#include <iostream>
#include <vector>
using namespace std;
const int N = 500+21;
const int MAX = 1500+1;
int t;
void solve()
{
    int n;
    cin>>n;
    int a[N+2];
    int pos[N+2];
    int vis[N]; 

    for (int i=1; i<=n; i++)
    {
        cin>>a[i];
        pos[a[i]] = i;
    }
    a[n+1] = n+1;
    pos[n+1] = n+1;
    int operations = 0;
    //cout<<"aaa"<<endl;
    vector<int> ans;
    for (int i=1; i<n+1; i++)
    {
        if (a[i] != i)
        {
            int curr = pos[i];
            int prev = n+1;
            while (curr != n+1 && operations < MAX)
            {
                //cout<<curr<<" ";
                int next = pos[curr];
                ans.push_back(curr);
                swap(a[prev], a[curr]);
                pos[a[prev]] = prev;
                pos[a[curr]] = curr;
                prev = curr;
                curr = next;
                
                operations++;
            }
            if (curr == n+1)
            {
                ans.push_back(curr);
                swap(a[prev], a[curr]);
                pos[a[prev]] = prev;
                pos[a[curr]] = curr;
                operations++;
            }
        }
    }
    if (operations < MAX)
    {
        cout<<operations<<endl;
        for (int i=0; i<ans.size(); i++)
            cout<<ans[i]<<" ";
        cout<<endl;
    }
    
}
int main()
{
    cin>>t;
    while (t--)
    {
        solve();
    }
}