/*
    One of the most popular children's toys sold by StartLink is the game Bead Escape. The game is played on a rectangular board with one red bead and one blue bead placed on it. The objective is to get the red bead into a hole on the board while ensuring that the blue bead does not fall in.

    Game Rules
    The board is a grid of size N x M, where each cell is 1x1 in size.
    The borders of the board are walls (#), and there is exactly one hole (O) on the board.
    The red (R) and blue (B) beads each occupy one full cell.
    You cannot move the beads directly — instead, you tilt the entire board in one of four directions: up, down, left, or right.
    When the board is tilted, both beads roll in that direction until they either hit a wall or fall into the hole.
    The beads move simultaneously and cannot occupy the same cell at the same time.
    If the red bead falls into the hole, the move is considered successful — but only if the blue bead does not fall in.
    If the blue bead falls into the hole at any time (even simultaneously with the red bead), the move fails.
    A tilt ends when both beads can no longer move.
    
    Given the initial configuration of the board, determine the minimum number of moves needed to get the red bead into the hole while ensuring the blue bead does not fall in. You can make at most 10 moves. If it is not possible to succeed within 10 moves, output -1.

    The first line contains two integers N and M (3 ≤ N, M ≤ 10), the number of rows and columns of the board.
    The next N lines each contain a string of length M representing the board:
    #: Wall (beads cannot pass through)
    .: Empty space
    O: Hole
    R: Red bead
    B: Blue bead
    There will always be exactly one R, one B, and one O. The outer border of the board will always be composed of walls (#).

    Output a single integer — the minimum number of moves needed to get the red bead into the hole without the blue bead falling in.
    If it's not possible within 10 moves, output -1.
    
    Example
    
    Input
    5 5
    #####
    #..B#
    #.#.#
    #RO.#
    #####

    Output
    1

*/

#include <iostream>
using namespace std;
const int N = 22;
int board[N][N];
bool visited[N][N][N][N];
int n, m;
char s;
int red_x, red_y;
int blue_x, blue_y;
int hole_x, hole_y;
int answer = N;
void move_balls(int r_x, int r_y, int b_x, int b_y, int depth, int dir)
{    
    visited[r_x][r_y][b_x][b_y] = true;
    if (depth > 10)
        return;
    
    for (int i=0; i<4; i++)
    {
        int m_r_x = r_x, m_r_y = r_y;
        int m_b_x = b_x, m_b_y = b_y;
        bool b_hole = false, r_hole = false;
        int r_count=0, b_count=0;
        if (i == 0)
        {
            while (!board[m_r_x][m_r_y+1])
            {
                m_r_y++;
                r_count++;
                if (m_r_x == hole_x && m_r_y == hole_y)
                    r_hole = true;
            }
            while (!board[m_b_x][m_b_y+1])
            {
                m_b_y++;
                b_count++;
                if (m_b_x == hole_x && m_b_y == hole_y)
                    b_hole = true;
            }
            
            if (m_b_x==m_r_x && m_b_y==m_r_y)
            {
                if (r_count>b_count)
                    m_r_y--;
                else
                    m_b_y--;
            }
        }
        else if (i == 1)
        {
             while (!board[m_r_x][m_r_y-1])
            {
                m_r_y--;
                r_count++;
                if (m_r_x == hole_x && m_r_y == hole_y)
                    r_hole = true;
            }
            while (!board[m_b_x][m_b_y-1])
            {
                m_b_y--;
                b_count++;
                if (m_b_x == hole_x && m_b_y == hole_y)
                    b_hole = true;
            }
            if (m_b_x==m_r_x && m_b_y==m_r_y)
            {
                if (r_count>b_count)
                    m_r_y++;
                else
                    m_b_y++;
            }
        }
        else if (i==2)
        {
            while (!board[m_r_x+1][m_r_y])
            {
                m_r_x++;
                r_count++;
                if (m_r_x == hole_x && m_r_y == hole_y)
                    r_hole = true;
            }
            while (!board[m_b_x+1][m_b_y])
            {
                m_b_x++;
                b_count++;
                if (m_b_x == hole_x && m_b_y == hole_y)
                    b_hole = true;
            }
            if (m_b_x==m_r_x && m_b_y==m_r_y)
            {
                if (r_count>b_count)
                    m_r_x--;
                else
                    m_b_x--;
            }
        }
        else if (i == 3)
        {
            while (!board[m_r_x-1][m_r_y])
            {
                m_r_x--;
                r_count++;
                if (m_r_x == hole_x && m_r_y == hole_y)
                    r_hole = true;
            }
            while (!board[m_b_x-1][m_b_y])
            {
                m_b_x--;
                b_count++;
                if (m_b_x == hole_x && m_b_y == hole_y)
                    b_hole = true;
            }
            if (m_b_x==m_r_x && m_b_y==m_r_y)
            {
                if (r_count>b_count)
                    m_r_x++;
                else
                    m_b_x++;
            }
        }
        
        if (b_hole)
        {

        }
        else if (r_hole)
        {
            answer = min(answer, depth);
        }
        else
        {
            move_balls(m_r_x, m_r_y, m_b_x, m_b_y, depth+1, 4);
        }
  

    }
}
void solve()
{
    move_balls(red_x, red_y, blue_x, blue_y, 1, 4);
}


void prepare_board()
{
    for (int i=0; i<=n+1; i++)
    {
        board[i][0] = 1;
        board[i][m+1] = 1;
    }
    for (int i=0; i<=m+1; i++)
    {
        board[0][i] = 1;
        board[n+1][i] = 1;
    }
}
int main()
{
    cin>>n>>m;
    for (int i=1; i<=n; i++)
    {
        for (int j=1; j<=m; j++)
        {
            cin>>s;
            
            if (s == '#')
            {
                board[i][j] = 1;
            }
            else if (s == '.')
            {
                board[i][j] = 0;
            }
            else if (s == 'R')
            {
                board[i][j] = 0;
                red_x = i;
                red_y = j;
            }
            else if (s == 'B')
            {
                board[i][j] = 0;
                blue_x = i;
                blue_y = j;
            }
            else if (s == 'O')
            {
                board[i][j] = 0;
                hole_x = i;
                hole_y = j;
            }
        }
    }
    prepare_board();

    
    solve();
    
    if (answer == N)
        cout<<"-1";
    else
        cout<<answer;
}