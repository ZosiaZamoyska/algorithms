/*

# Problem: Prime Factorization
# The first line of input contains a natural number T (T <= 1000) – the number of numbers to factorize.
# Each of the next T lines contains a number n (2 <= n <= 10^9).
#
# For each number, output its prime factorization in the form:
# n = p1^a1 * p2^a2 * ... * pk^ak
# Omitting the exponent if it equals 1.

*/

#include <iostream>
#include <vector>
using namespace std;
vector<pair<int, int> > czynniki;
int n, t;
int main()
{
	cin>>t;
	while (t--)
	{
		cin>>n;
		int k = n;
		czynniki.clear();
		for (int i=2; i*i<=n; i++)
		{
	  		int licznik = 0;
	  		while (k%i == 0)
	  		{
	   			k/=i;
	   			licznik++;
	  		}
	  		if (licznik>0)
	    		czynniki.push_back(make_pair(i, licznik));
		}
		if (k > 1)
			czynniki.push_back(make_pair(k, 1));
		cout<<n<<" = ";
		for (int i=0; i<czynniki.size(); i++)
		{
	  		if (i>0)
	  			cout<<"*";
	  		cout<<czynniki[i].first; // 2^2 zamiast 2*2
	  		if (czynniki[i].second>1)
	  		{
	  			cout<<"^"<<czynniki[i].second;
	  		}
		}
		cout<<endl;
	}
}