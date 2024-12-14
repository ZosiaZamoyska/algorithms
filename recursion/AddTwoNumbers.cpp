/*
    Add two numbers, but they are a reversed list

    Example
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]

    Input: l1 = [0], l2 = [0]
    Output: [0]
    
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
*/ 

#include <iostream>
#include <vector>
using namespace std;
int n, m, a;
vector<int> l1;
vector<int> l2;
vector<int> add(int a, int b, int extra, int ind)
{
	//cout<<a<<" "<<b<<" "<<extra<<" "<<ind<<" "<<n<<endl;
    if (a == 0 && b == 0 && extra == 0)
        return vector<int>();
    
    int sum = a + b + extra;
    extra = (sum - sum%10)/10;
    sum %= 10;
    ind += 1;
    a = 0, b = 0;
    if (ind < n)
        a = l1[ind];
    if (ind < m)
        b = l2[ind];

    vector<int> result = add(a, b, extra, ind);
    result.push_back(sum);
    return result;
}
int main()
{
    cin>>n>>m;
    for (int i=0; i<n; i++)
    {
        cin>>a;
        l1.push_back(a);
    }
    for (int i=0; i<m; i++)
    {
        cin>>a;
        l2.push_back(a);
    }

    vector<int> answer = add(l1[0], l2[0], 0, 0);
    for (int i=0; i<answer.size(); i++)
    	cout<<answer[i]<<" ";
}