/*
We have an array of n numbers a0, a1, ..., a(n-1) (where ai is either 0 or 1).
- ai = 0 means a person joins the queue.
- ai = 1 means a person leaves the queue.

Our task is to determine the minimum number of people who had to be in the queue initially
so that this sequence of events is possible (i.e., there is never a moment when a person leaves an empty queue).

Example:
Input: n = 6
       arr = [1, 0, 1, 1, 0, 1]
Output: 2
*/

#include <iostream>
using namespace std;
const int N = 1000000+21;
int tab[N];
int n;
int queue_size = 0, min_queue_size = 0;
int main()
{
	cin>>n;
	for (int i=0; i<n; i++)
		cin>>tab[i];

	for (int i=0; i<n; i++)
	{
		if (tab[i] == 0)
			queue_size++;
		else
			queue_size--;
		min_queue_size = min(min_queue_size, queue_size);
    }
	cout<<-min_queue_size<<endl;
}