/*
    You are given t, number of testcases.

    For each testcase, find the following: 
    You are given left bottom corrner coordinates and upper top corner coordinates of three papers (white, black and black).
    The papers are placed on a grid as given. Check if after placing black papers, the white one is still visible.
    Coordinates have value up to 10^6 and are positive integers.
    Print YES or NO.

    Example: 
    4 7 5
    0 0 4 9
    0 1 4 6
    

    Answer: 
    YES
*/

#include <iostream>
#include <set>
#include <vector>
#include <map>
using namespace std;
int t;
void solve()
{
    int x[6], y[6];
    map<int, int> val_x, val_y;
    set<int> xs;
    set<int> ys;
    
    for (int i=0; i<3; i++){
        cin>>x[2*i]>>y[2*i]>>x[2*i+1]>>y[2*i+1];
        xs.insert(x[2*i]);
        xs.insert(x[2*i+1]);
        ys.insert(y[2*i]);
        ys.insert(y[2*i+1]);
    }
    
    int indx = 0;
   for (set<int>::iterator it=xs.begin(); it!=xs.end(); ++it)
   {
       val_x[*it] = indx++;
   }
   indx = 0;
   for (set<int>::iterator it=ys.begin(); it!=ys.end(); ++it)
   {
       val_y[*it] = indx++;
   }
   
   vector<vector<int> > matrix(10, vector<int>(10));
   for (int i=val_x[x[0]]; i<val_x[x[1]]; i++)
   {
       for (int j=val_y[y[0]]; j<val_y[y[1]]; j++)
            matrix[i][j] = 1;
   }
   for (int i=val_x[x[2]]; i<val_x[x[3]]; i++)
   {
       for (int j=val_y[y[2]]; j<val_y[y[3]]; j++)
        matrix[i][j] = 0;
   }
   for (int i=val_x[x[4]]; i<val_x[x[5]]; i++)
   {
       for (int j=val_y[y[4]]; j<val_y[y[5]]; j++)
            matrix[i][j] = 0;
   }
   for (int i=0; i<10; i++)
   {
       for (int j=0; j<10; j++)
        if (matrix[i][j] == 1)
        {
            cout<<"YES\n";
            return;
        }
   }
    cout<<"NO\n";
    return;
}
int main()
{
    cin>>t;
    while (t--)
    {
        solve();
    }
}