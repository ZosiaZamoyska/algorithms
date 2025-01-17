/*
    Bucket Fill tool implementation

    for an image, apply bucket fill to a pixel with a certain color
    print out result image
*/
#include <iostream>
using namespace std;
const int N = 1000+21;
int n, m, xi, yi, c, h;
int tab[N][N];
int x[4] = {-1, 0, 1, 0};
int y[4] = {0, -1, 0, 1};
bool valid(int a, int b)
{
    if (a>=0 && a<n && b>=0 && b<m && tab[a][b] == h)
        return true;
    return false;
}
void recolor(int a, int b)
{
    tab[a][b] = c;

    for (int i=0; i<4; i++)
    {
        if (valid(a+x[i], b+y[i]))
            recolor(a+x[i], b+y[i]);
    }
}
int main()
{
    cin>>n>>m;
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<m; j++)
            cin>>tab[i][j];
    }
    cin>>xi>>yi>>c;
    h = tab[xi][yi];
    recolor(xi, yi);
    for (int i=0; i<n; i++)
    {
    	for (int j=0; j<m; j++)
    		cout<<tab[i][j]<<" ";
    	cout<<endl;
    }
}