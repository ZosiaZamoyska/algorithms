/*
    Longest Increasing Path In A Matrix

    Find longest path that has increasing value in each consecutive cell
*/
#include <iostream>
#include <vector>
#include <algorithm>
const int N = 1000+21;
using namespace std;
int n, m;
int tab[N][N];
int ans[N][N];
int dfs(int i, int j, int prev)
{
  if (i<0 || j < 0 || i==n || j==m)
  	return 0;

	if (tab[i][j] <= prev)
  	return 0;
    
  if (ans[i][j] > 0)
  	return ans[i][j];
  
  int curr = tab[i][j];
  int ans1 = dfs(i+1, j, curr);
  int ans2 = dfs(i-1, j, curr);
  int ans3 = dfs(i, j+1, curr);
  int ans4 = dfs(i, j-1, curr);
  ans[i][j] =  max({ans1, ans2, ans3, ans4}) + 1;
  return ans[i][j];
}
int main()
{
    cin>>n>>m;
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<m; j++)
        {
            cin>>tab[i][j];
        }
    }

	int odp = 0;
	for (int i=0; i<n; i++)
    {
        for (int j=0; j<m; j++)
        {
            odp = max(odp, dfs(i, j, 0));
        }
    }
    cout<<odp<<endl;
}