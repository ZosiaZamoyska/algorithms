#include <iostream>
using namespace std;
const int N = 505;
int n, m, q, a1, a2, b1, b2;
int a[N][N];
int pref[N][N];

void prefiks()
{
	for (int i=1; i<=n; i++)
	{
		for (int j=1; j<=m; j++)
		{
			pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + a[i][j];
		}
	}
}

int oblicz(int x1, int y1, int x2, int y2)
{
	return pref[x2][y2] - pref[x1-1][y2] - pref[x2][y1-1] + pref[x1-1][y1-1];
}

int main() {
	
	cin>>n>>m;
	for (int i=1; i<=n; i++)
	{
		for (int j=1; j<=m; j++)
		{
			cin>>a[i][j];
		}
	}
	
	prefiks();
	for (int i=0; i<=n; i++)
	{
		for (int j=0; j<=m; j++)
			cout<<pref[i][j]<<" ";
		cout<<endl;
	}
	cin>>q;
	for (int i=0; i<q; i++)
	{
		cin>>a1>>b1>>a2>>b2;
		cout<<oblicz(a1, b1, a2, b2)<<endl;
	}
	return 0;
}
