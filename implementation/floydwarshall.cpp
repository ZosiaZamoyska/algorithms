#include <iostream>
using namespace std;
const int N = 1000+21;
const int INF = 1000000000+21;
int n, m, a, b, c;
int dist[N][N];

void floydWarshall()
{
    for (int k=1; k<=n; k++)
    {
        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=n; j++)
            {
                // check if (i->j) > (i->k) + (k->j) and update
                // unless (i->k) or (k->j) are undefined
                if (dist[i][j] > dist[i][k] + dist[k][j] && dist[k][j]!=INF && dist[i][k]!=INF)
                    dist[i][j] = dist[i][k] + dist[k][j];
                
            }
        }
    }
}

int main()
{
    cin>>n>>m;

    for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++)
        {
            if (i==j)
                dist[i][j] = 0;
            else
                dist[i][j] = INF;
        }

    for (int i=0; i<m; i++)
    {
        cin>>a>>b>>c;
        dist[a][b] = c;
        //dist[b][a] = c; // bi-directional graph version
    }

    floydWarshall();

    for (int i=1; i<=n; i++)
    {
        for (int j=1; j<=n; j++)
            cout<<dist[i][j]<<" ";
        cout<<endl;
    }
}