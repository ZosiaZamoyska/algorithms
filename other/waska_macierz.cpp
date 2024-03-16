//
//  main.cpp
//  waska macierz
//
//  Created by Złosia  on 04.12.2017.
//  Copyright © 2017 Złosia . All rights reserved.
//

#include <iostream>
using namespace std;
const int N=2*100*1000+21;
int x;
long long int tmp;
int tab[3][N];
long long int dp[3][N];
long long int wyznacz_maxi(int i, int j)
{
    if (i==0)
    {
        return max(dp[1][j-1], dp[2][j-1]);
    }
    else
    {
        if (i==1)
        {
            return max(dp[0][j-1], dp[2][j-1]);
        }
        else
        {
            return max(dp[0][j-1], dp[1][j-1]);
        }
    }
}
int main()
{
    cin>>x;
    for (int j=1; j<=x; j++)
    {
        for (int i=0; i<3; i++)
        {
            cin>>tab[i][j];
        }
    }
    for (int j=1; j<=x; j++)
    {
        for (int i=0; i<3; i++)
        {
            tmp=wyznacz_maxi(i, j);
            dp[i][j]=tmp+tab[i][j];
        }
    }
    cout<<max(dp[0][x], max(dp[1][x], dp[2][x]))<<"\n";
    return 0;
}
