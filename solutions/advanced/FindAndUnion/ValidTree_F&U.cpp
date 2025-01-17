/*
    Check if given graph is a valid tree (Find and Union)
*/

#include <iostream>
using namespace std;
const int N = 100000+21;
int parent[N];
int n, m, a, b;

int find(int i)
{
	if (parent[i] == i)
  	return i;
  else
  {
  	int ans = find(parent[i]);
    parent[i] = ans;
    return parent[i];
  }
}

int main()
{
	cin>>n>>m;
  for (int i=0; i<n; i++)
  	parent[i] = i;
    
  if (m == n-1)
  {
  	bool odp = true;
		for (int i=0; i<m; i++)
    {
    	cin>>a>>b;
      int a_par = find(a);
      int b_par = find(b);
      if (a_par == b_par)
      {
        odp = false;
      }
      parent[a] = b;
    }
    
    if (odp)
    {
    	cout<<"TRUE\n";
    }
    else
    {
    	cout<<"FLASE\n";
    }
	}
  else
  {
  	for (int i=0; i<m; i++)
    {
    	cin>>a>>b;
    }
  	cout<<"FALSE\n";
  }
}
