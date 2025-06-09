#include <iostream>
#include <vector>
using namespace std;
const int N = 200000+21;
int n, q, nodes;
string s;
char mapped_letter[N];
vector<int> graph[N];
string odp;
void addWord(string s, int ind, int node)
{
    if (ind == s.length())
        return;
    int index = -1;
    int k = -1;
    for (int i=0; i<graph[node].size(); i++)
    {
        k = graph[node][i];
        if (mapped_letter[k] == s[ind])
            index = k;
    }
    if (index != -1)
    {
        addWord(s, ind+1, k);
    }
    else
    {
        nodes++;
        mapped_letter[nodes] = s[ind];
        graph[node].push_back(nodes);
    }
}

int findWords(string s, int ind, int node, string ans)
{
    if (ind == s.length())
    {
        odp = ans;
        return 1;
    }
    if (s[ind] != '?')
    {
        int index = -1;
        int k = -1;
        for (int i=0; i<graph[node].size(); i++)
        {
            k = graph[node][i];
            if (mapped_letter[k] == s[ind])
                index = k;
        }
        if (index==-1)
            return 0;
        else
        {
            return findWords(s, ind+1, k, ans+mapped_letter[k]);
        }
    }
    else
    {
        int k;
        int wynik = 0;
        for (int i=0; i<graph[node].size(); i++)
        {
            k = graph[node][i];
            int tmp_wyn = findWords(s, ind+1, k, ans+mapped_letter[k]);
            wynik += tmp_wyn;
        }
        return wynik;
    }
    return 0;
}

int main()
{
    cin>>n;
    for (int i=0; i<n; i++)
    {
        cin>>s;
    }
    cin>>q;
    for (int i=0; i<q; i++)
    {
        cin>>s;
        int liczba = findWords(s, 0, 0, "");
        if (liczba == 1)
            cout<<odp<<endl;
        else
            cout<<liczba<<endl;
    }
}