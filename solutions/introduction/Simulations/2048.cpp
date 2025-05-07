/*
    2048 is a fun single-player game played on an N x N board. In this game, the player moves all the blocks on the board in one of four directions — up, down, left, or right. When two blocks with the same value collide during a move, they merge into one block with a value equal to their sum. However, a block can only merge once per move.

    In this version of the game:

    No new blocks are added after each move (unlike the original 2048 game).
    If three identical blocks are lined up in a direction, only the leading pair will merge first (e.g., [2, 2, 2] moving left becomes [4, 2], not [2, 4]).
    Your goal is to determine the maximum block value that can be created after performing at most 5 moves.
    You are given the initial state of the board. Write a program to find the largest possible block value obtainable in five or fewer moves.

    Input
    The first line contains an integer N (1 ≤ N ≤ 20), the size of the board.
    The next N lines each contain N integers representing the initial board state. Each number is:
    0 for an empty cell, or
    A power of 2 (e.g., 2, 4, 8, ..., 1024), representing a block's value.
    There will be at least one non-zero block on the board.

    Output
    Output a single integer: the largest block value that can be created with at most five moves.

    Example
    3
    2 2 2
    4 4 4
    8 8 8

    Answer:
    16

    https://www.acmicpc.net/problem/12100
*/

#include <iostream>
#include <queue>
using namespace std;
const int N = 21;
struct node {
    int value;
};

int n, a;

// compress a queue column or row
queue<int> compute_unit(queue<int>& input)
{
    queue<int> output;
    int curr = input.front(); 
    int next = -1;
    input.pop();
    while (!input.empty())
    {
        next = input.front();
        if (curr == next)
        {
            output.push(2*curr);
            curr = -1;
        }
        else
        {
            if (curr != -1)
                output.push(curr);
            curr = next;
        }
        input.pop();
    }
    if (curr != -1)
        output.push(curr);
    return output;
}

// 0 - up, 1 - down, 2 - right, 3 - left
vector<vector<node> > compute_array(const vector<vector<node> >& in, int direction)
{
    vector<vector<node> > out(n, vector<node>(n));
    vector<queue<int>> units(n);

    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
        {
            if (direction == 0 && in[i][j].value != 0) 
                units[j].push(in[i][j].value);
            else if (direction == 1 && in[n-i-1][j].value != 0)
                units[j].push(in[n-i-1][j].value);
            else if (direction == 2 && in[i][j].value != 0)
                units[i].push(in[i][j].value);
            else if (direction == 3 && in[i][n-j-1].value != 0)
                units[i].push(in[i][n-j-1].value);
            
        }
    }
    for (int i=0; i<n; i++)
    {
        queue<int> tmp;
        if (!units[i].empty())
            tmp = compute_unit(units[i]);
        int index = 0;
        while (!tmp.empty())
        {
            if (direction == 0)
                out[index++][i].value = tmp.front();
            else if (direction == 1)
                out[n-index++-1][i].value = tmp.front();
            else if (direction == 2)
                out[i][index++].value = tmp.front();
            else if (direction == 3)
                out[i][n-index++-1].value = tmp.front();
                
            tmp.pop();
        }
    }
    return out;
}

int max_array(const vector<vector<node> >& in)
{
    int max_value = 0;
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
        {
            max_value = max(max_value, in[i][j].value);
        }
    }
    return max_value;
}

int max_all_combinations(const vector<vector<node> >& in, int prev_direction, int depth)
{
    if (depth >= 5)
    {
        return max_array(in);
    }
    
    int max_answer = 0;
    for (int dir=0; dir<4; dir++)
    {
        max_answer = max(max_answer, max_all_combinations(compute_array(in, dir), dir, depth+1));            
    }
    return max_answer;
}

int main()
{
    cin>>n; 
    vector<vector<node>> tab(n, vector<node>(n));
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
        {
            cin>>a;
            tab[i][j].value = a;
        }
    }
    
    cout<<max_all_combinations(tab, -1, 0);
}