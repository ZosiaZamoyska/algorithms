/*
    You are given a t, number of test cases.
    For each testcase, you are given a string s.
    Find minimum number of 'x' that need to be inserted into s so it becomes a palindrome.
    Print -1 if not possible.

    Input
    3
    ax
    abc
    abccba

    Output:
    1
    -1
    0
*/

#include <iostream>
using namespace std;
int t;
int solve()
{
    string s;
    cin>>s;
    string no_x_s = "";
    int n = s.length();
    for (int i=0; i<n; i++)
    {
        if (s[i] != 'x')
            no_x_s += s[i];
    }
    bool is_palindrome = true;
    int l = no_x_s.length(); 
    for (int i=0; i<l/2; i++)
    {
        if (no_x_s[i] != no_x_s[l-i-1])
            is_palindrome = false;
    }
    if (!is_palindrome)
        return -1;
        
    int front = 0;
    int back = n-1;
    int count = 0;
    while (front < back)
    {
        if (s[front] == s[back])
        {
            front++;
            back--;
        }
        else
        {
            if (s[front] == 'x')
            {
                count++;
                front++;
            }
            else if (s[back] == 'x')
            {
                count++;
                back--;
            }
        }
    }
    return count;
}
int main()
{
    cin>>t;
    while (t--)
    {
        cout<<solve()<<endl;
    }
}