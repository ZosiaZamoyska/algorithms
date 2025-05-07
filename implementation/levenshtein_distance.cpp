#include <iostream>
#include <vector>
using namespace std;
const int N = 500+21;
int find_distance(string a, string b)
{
    vector<vector<int> > dp(N, vector<int>(N));
    int n = a.length();
    int m = b.length();
    for (int i=0; i<=n; i++)
    {
        for (int j=0; j<=m; j++)
        {
            if (i==0)
                dp[i][j] = j;
            else if (j==0)
                dp[i][j] = i;
            else if (a[i-1] == b[j-1])
                dp[i][j] = dp[i-1][j-1];
            else 
            {
                dp[i][j] = 1 + min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]);
            }
        }
    }
    return dp[n][m];
}

int main()
{
    string s1 = "ABCXYZDEFABCDEF";
    string s2 = "ABCDEFABCDEF";
    cout<<find_distance(s1, s2)<<endl;
}