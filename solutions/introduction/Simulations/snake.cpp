/*
    There is a DOS game called "Dummy", where a snake moves around a square board. The snake grows longer whenever it eats an apple. The game ends when the snake crashes into a wall or its own body.

    The game takes place on an N x N board. Some of the board cells contain apples. The edges of the board are surrounded by walls. At the start of the game, the snake is located in the top-left corner (row 1, column 1) and is initially facing right. The snake starts with a length of 1.

    Each second, the snake performs the following actions:

    1. It moves forward by one cell in its current direction, increasing its length.
    2. If it moves into a wall or its own body, the game ends.
    3. If the new cell contains an apple:
        a. The apple is eaten and disappears.
        b. The tail does not move, so the snake’s length increases by 1.
    4. If the new cell does not contain an apple:
        a. The tail moves forward (i.e., the last segment is removed), so the snake’s length stays the same.
    
    You're given the positions of the apples and a schedule of direction changes. Your task is to simulate the game and determine how many seconds elapse before the game ends.

    Input
    The first line contains an integer N (2 ≤ N ≤ 100), the size of the board.
    The second line contains an integer K (0 ≤ K ≤ 100), the number of apples.
    The next K lines each contain two integers r and c (1-based indexing), the row and column positions of apples. No apple is placed at the starting position (1, 1).
    The next line contains an integer L (1 ≤ L ≤ 100), the number of direction changes.
    The next L lines each contain a time X (1 ≤ X ≤ 10,000) and a character C:
    C is 'L' (turn left) or 'D' (turn right).
    This indicates that after X seconds, the snake turns 90 degrees in the given direction.
    
    Output
    Output a single integer: the number of seconds that elapse until the game ends.

    https://www.acmicpc.net/problem/3190
*/

#include <iostream>
#include <vector>
using namespace std;
const int N = 100+21;
const int M = 10000+21;
struct snake {
    int x, y;
    snake* prev;
    snake* next;
};


int n, k, m, a, b;
char dir, moves[M];
int answer = 0;
vector<vector<int> > board(N, vector<int> (N, 0));
void move_snake(snake* head)
{
    //cout<<"snake moves"<<endl;
    int new_x = head->x;
    int new_y = head->y;
    snake* curr = head->prev;
    while (curr != nullptr)
    {
        //cout<<new_x<<" "<<new_y<<endl;
        swap(curr->x, new_x);
        swap(curr->y, new_y);
        curr = curr->prev;
    }
    return;
}
void solve()
{
    snake* head = new snake{1, 0, nullptr, nullptr};
    snake* tail = new snake{1, 0, nullptr, nullptr};
    head->prev = tail;
    board[1][0] = 1;
    int direction = 0;
    // 0 -> 1 down 2 up 3 <-
    for (int i=-1; i<M; i++)
    {
        board[1][0] = 1;

        //cout<<i<<": "<<head->x<<" "<<head->y<<" "<<tail->x<<tail->y<<endl;
        answer = i+1;
        if (moves[i])
        {
            if (moves[i] == 'D')
                direction = (direction + 1) % 4;
            else
                direction = (direction + 3) % 4;
        }
        if (direction == 0)
        {
            head->y++;
        }
        else if (direction == 1)
        {
            head->x++;
        }
        else if (direction == 2)
        {
            head->y--;
        }
        else if (direction == 3)
        {
            head->x--;
        }
        if (board[head->x][head->y] == 1)
        {
            return;
        }
        snake *new_tail = nullptr;
        if (board[head->x][head->y] != 2)
        {
            board[tail->x][tail->y] = 0;
        }
        else
        {
            new_tail = new snake{tail->x, tail->y, nullptr, nullptr};
        }
        move_snake(head);
        if (new_tail != nullptr)
        {
            tail->prev = new_tail;
            tail = new_tail;
        }
        board[head->x][head->y] = 1;
    }
}

void prepare_board()
{
    for (int i=0; i<n+1; i++)
    {
        board[0][i] = 1;
        board[i][0] = 1;
        board[n+1][i] = 1;
        board[i][n+1] = 1;
    }
}

int main()
{
    cin>>n;
    
    cin>>k;
    for (int i=0; i<k; i++)
    {
        cin>>a>>b;
        board[a][b] = 2; 
    }
    prepare_board();
    
    cin>>m;
    for (int i=0; i<m; i++)
    {
        cin>>a>>dir;
        moves[a] = dir;
    }
    
    solve();
    cout<<answer<<endl;
}