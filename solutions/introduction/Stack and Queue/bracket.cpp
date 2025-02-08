/*
A non-uniform bracket sequence is any permutation of opening and closing brackets: 
- round (), 
- square [], 
- curly {}.

A bracket sequence is correct if it can be completed with numbers and operations 
such that the mathematical expression is valid.

Example:
- "{[()()]}" is correct.
- "([)()]" is incorrect.

Task: Determine whether each input bracket sequence is correct.

Input:
- N (1 ≤ N ≤ 1000) — the number of bracket sequences to check.
- N sequences, each of length between 1 and 250 characters.

Output:
- Print "YES" if the sequence is correct, otherwise print "NO".

Example:
Input:
2
{[()()]}
([)()]

Output:
YES
NO
*/

#include <iostream>
#include <stack>
#include <map>

using namespace std;

int main() 
{
    int n;
    cin >> n;
    
    map<char, int> M = {{'(', 1}, {')', -1}, {'[', 2}, {']', -2}, {'{', 3}, {'}', -3}};
    
    for (int i = 0; i < n; i++) 
    {
        string s;
        cin >> s;
        
        stack<int> S;
        bool odp = true;

        for (char c : s)
        {
            if (M[c] > 0) 
            {
                S.push(M[c]);
            } else {
                if (S.empty()) 
                {
                    odp = false;
                    break;
                }

                int otw = S.top();
                S.pop();
                int zam = M[c];

                if (otw + zam != 0) 
                {
                    odp = false;
                    break;
                }
            }
        }

        if (!S.empty()) odp = false;

        cout << (odp ? "YES" : "NO") << endl;
    }

    return 0;
}
