# Table of Contents
- [Teaching solutions](#teaching-solutions)
  - [Introduction to Algorithms](#introduction-to-algorithms)
    - [Element Occurance](#element-occurance)
    - [Prefix Sum](#prefix-sum)
    - [Sorting](#sorting)
    - [Stack and Queue](#stack-and-queue)
    - [Leader Search](#leader-search)
    - [Maximum Subarray Sum](#maximum-subarray-sum)
    - [Prime and Composite Numbers](#prime-and-composite-numbers)
    - [Greatest Common Divisor](#greatest-common-divisor)
    - [Fibonacci](#fibonacci)
    - [Recursion](#recursion)
    - [Binary Search](#binary-search)
    - [Two-Pointer Technique](#two-pointer-technique)
    - [Greedy](#greedy)
    - [Dynamic Programming](#dynamic-programming)
    - [Compression](#compression)
    - [Simulations](#simulations)
  - [Advanced Algorithms](#advanced-algorithms)
    - [Binary Tree](#binary-tree)
    - [DFS](#dfs)
    - [Dijkstra](#dijkstra)
    - [Find and Union](#find-and-union)
    - [MST](#mst)
    - [Topological Sort](#topological-sort)
    - [DP on a Tree](#dp-on-a-tree)
- [Implementation](#implementation)
  - [Sorting](#sorting-1)
  - [Graphs](#graphs)
  - [Other](#other)
- [Testing](#testing)

# Teaching solutions

Keeping solutions of different problems by topic.

## Introduction to Algorithms

### Element Occurance
<details>
<summary>Buttons</summary>
Print out press count of each button from 1 to n (count how many times each button was pressed), including that n+1th button resets all values to maximum of all from 1 to n.

Example Input:
5 7 
3 4 4 6 1 4 4 

Example Output:
3 2 2 4 2
</details>

<details>
<summary>Frog</summary>
A frog can cross a river, if all leaves on position from 1 to n exist. Knowing the order of leaf falling, print out when will crossing be possible.
Example Input:
5 8
1 3 1 4 2 3 5 4

Example Output:
7
</details>
<details>
<summary>Is Permutation</summary>
Check if given sequence of n integers is a permutation of a set from 1 to n. Print out yes or no.
</details>
<details>
<summary>Swap</summary>
Given two arrays A and B, print if it's possible to swap an element of A with an element of B to have two lists of equal sum.
</details>
<details>
<summary>Unique Count</summary>
Check if for a list of numbers, each number occurs unique amount of time, that is: there is no other number that occurs the same amount of times. (OK: 1 2 2 3 3 3, NOT OK: 1 1 2 2)
</details>

### Prefix Sum

<details>
<summary>Maximum Mushrooms Collection</summary>
Given a list of n integers, where each value represents the number of mushrooms at that position along a path. A gatherer stands at position k and can make m moves (each move is left or right). Find the maximum mushrooms that can be collected.
</details>

<details>
<summary>Tape</summary>
Given a tape with a list of n integers (1 <= n <= 1,000,000), a boy tries to find the minimum possible arithmetic mean of any contiguous subarray.
</details>

<details>
<summary>Passing Cars</summary>
Count how many pairs of passing cars exist (cars traveling in opposite directions meeting at the same point), given a list of n cars in order and their travel direction (0 - east. 1 - west).
</details>

<details>
<summary>Hamsters</summary>
Count how many pairs of passing cars exist (cars traveling in opposite directions meeting at the same point), given a list of n cars in order and their travel direction (0 - east. 1 - west).
</details>

<details>
<summary>Count Vowels</summary>
Count vowels in a word on different query ranges.
</details>

### Sorting

<details>
<summary>Unique count</summary>
We are given a sequence of n >= 0 integers a0, a1, a2, ..., a(n-1), where -2 * 10^9 <= ai <= 2 * 10^9. 
The task is to calculate how many distinct numbers appear in this sequence.
</details>

<details>
<summary>Multiplication</summary>
Find values x, y, z from a list, such that their product is as large as possible. Do it m times. 
</details>

<details>
<summary>Nails</summary>
You are given a board with nails sticking out at different heights. Each nail has a specific sticking-out length. 
Additionally, you are allowed to "nail" (reduce the height of) up to k nails, lowering them to any height less than or equal to their current height. The task is to determine the maximum number of nails that can stick out at the same height after using up to k nailing opportunities.</details>

<details>
<summary>Minimum Distance</summary>
In Bajtocja, railway tracks run in a straight line from east to west. The houses of the residents are located to the north of the railway track.
If two people from different houses want to meet, they meet at the midpoint of the distance between their houses. However, this distance is not calculated in a traditional way as a straight-line segment between the houses.
Instead, the distance is determined as follows: a person first walks south to the railway tracks, then along the tracks to the line where the target house is located, and finally walks straight north to that house.
From all possible pairs of houses, we want to find the pair for which this distance is minimal.
</details>

### Stack and Queue

<details>
<summary>Initial Size of a Queue</summary>
Determine the minimum number of people who had to be in the queue initially, knowing the order of peopele joining and leaving a queue. We do not know how many people were there initially, but there should not be a moment where a person leaves an empty queue.
</details>

<details>
<summary>Brackets</summary>
Determine whether each input bracket sequence is correct.
</details>

<details>
<summary>Fish</summary>
Fishes of different sizes swim upstream and downstream. If they meet, bigger fish eats the smaller one. Calculate number of survivors. 
</details>

<details>
<summary>Queue Bribe</summary>
A boy wants to be the first in the queue. Each person has a price. Calculate the cheapest way the boy can be first in the queue.
</details>

### Leader Search

<details>
<summary>Tape</summary>
A boy found a long tape at home and, without hesitation, wrote a sequence of integers on it. He wants to cut the tape in some places, but there is a strict condition:
A cut can only be made if both parts of the tape have the same leader.
A leader of a sequence is an element that appears more than half the times in that sequence.
Your task is to determine the number of valid cut positions where both the left and right parts of the tape have the same leader.
</details>

<details>
<summary>Flag</summary>
A flag consists of `n` horizontal stripes, each with a different color. The king wants to change the flag so that it consists of `n` stripes in only two alternating colors (A and B). 
The goal is to minimize the number of stripes that need to be repainted. The choice of colors does not matter, but the colors must alternate.
</details>

<details>
<summary>Prefix Leader</summary>
A prefix leader is an element that is a leader for more than half of prefixes. Find, if exists, the prefix leader.
</details>

### Maximum Subarray Sum

<details>
<summary>Weight Loss</summary>
Find a segment from a weight loss diary where the weight loss is biggest and print out the difference.
</details>

<details>
<summary>Best Trip</summary>
A boy is traveling between cities on a line. He wants to earn as much as possible, and he knows how much exactly he will earn or lose on each road between cities. He also has a train ticket, that can take him from any station to any other station (even back, so he can earn twice). Calculate maximum profit he can earn.
</details>

<details>
<summary>Homework</summary>
Given a sequence of numbers, circle three values on positions a, b, and c such that sum between positions a and b and b and c (without circled values) is largest.
</details>

### Prime and Composite Numbers

<details>
<summary>Coins</summary>
There are n coins, numbered from 1 to n, on the table and n people.
Each person from 1 to n, flips certain coins.
To be specific, i-th person flips coins numbered i, 2*i, 3*i, ..., etc.
How many coins will be flipped at the end?
</details>

<details>
<summary> Kth Factor</summary>
You are given two positive integers n and k. 
A factor of an integer n is defined as an integer i where n % i == 0.
Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
</details>

<details>
<summary>Perimeter</summary>
What is a minimum perimeter of a rectangle with a area of exactly p?
</details>

<details>
<summary>Peaks</summary>
A boy is packing for an expedition to the Mountains. 
He already has a map of the route he will follow. 
These are n consecutive places located at certain heights. 
A peak is a place for which two neighboring places are lower. 
We assume that the first and last place are not peaks. 
The boy would like to divide the entire route into coherent sections with the same number of places. 
In each section, he would like to place exactly one flag. 
He decided that he can mix up the flags only on the peaks. 
Help the boy and calculate the maximum number of flags he can place. 
</details>

<details>
<summary>Flags</summary>
A boy is packing for an expedition to the Mountains. 
He already has a map of the route he will follow. 
These are n consecutive places located at certain heights. 
A peak is a place for which two neighboring places are lower. 
We assume that the first and last place are not peaks. 
The boy wants to place flags on the peaks. 
He decides that if he takes k flags with him, then the distance between any two flags must be at least k. 
Places x < y are exactly y-x apart. 
Help the boy and calculate the maximum number of flags he can place. 
We know that the boy has an unlimited number of flags that he can take on his expedition.
</details>

### Sieve of Erastosthenes

<details>
<summary>Half-primes</summary>
A half-prime number is a number that is the product of exactly two prime numbers.
We receive queries asking how many half-prime numbers exist in the range [a, b].
</details>

<details>
<summary>Factorization</summary>
The first line of input contains a natural number T (T <= 1000) – the number of numbers to factorize.
Each of the next T lines contains a number n (2 <= n <= 10^9).
For each number, output its prime factorization in the form:
n = p1^a1 * p2^a2 * ... * pk^ak
</details>

<details>
<summary>Prime Prefix</summary>
To prove that you can quickly find prime numbers, calculate the sum of prime numbers in the interval [a, b], for various given a and b.
</details>

<details>
<summary>Number Array</summary>
We are given an array containing n integers a0, a1, ..., an-1. 
For each number ai, we want to count how many elements from the array are not divisors of it.
</details>

<details>
<summary> </summary>
Recall that a **perfect number** is a natural number greater than 1 that is equal to the sum of all its proper divisors. 
A **second-kind perfect number** is a natural number greater than 1 that is equal to the product of all its proper divisors. 
For example, proper divisors of 27 are 1, 3, and 9, and since 1 * 3 * 9 = 27, 27 is a second-kind perfect number.
A proper divisor of a number is a natural divisor other than the number itself.
We would like to know **how many second-kind perfect numbers are contained in certain ranges**.
</details>

### Greatest Common Divisor

<details>
<summary>Boys</summary>
Three boys each have coins of denominations a, b, and c respectively (each boy has only one type of coin).
They want to find the smallest possible amount of money that each of them can pay using only their coins.
</details>

<details>
<summary>Tangerines</summary>
A boy collects tangerines into two baskets with capacity up to 'n'. His reward is GCD(x, y) + LCM(x, y).
Goal: Find x, y ≤ n to maximize the reward.
</details>

<details>
<summary>Monkey</summary>
A cheerful monkey found a new game. She arranged n cages with animals (each cage contains exactly one animal) in a circle 
and jumps over them. The monkey always jumps over d consecutive cages and always opens the one she lands on. 
She stops when she jumps on a cage that has already been opened. 
Your task is to determine how many animals will be released. 
</details>

<details>
<summary>Prime Set</summary>
We are given two integers a and b. We want to check whether the set of prime divisors of a is a subset of the set of prime divisors of b. The set of prime divisors of a number includes every prime number that divides it.
</details>

### Fibonacci

<details>
<summary>Prime Set</summary>
Given a list of numbers x0, x1, ..., xm, check whether each number can be expressed as the sum of two Fibonacci numbers.
</details>

<details>
<summary>Rabbit</summary>
A rabbit is jumping on a straight path using Fibonacci number lengths as jumps. Some positions contain stones where the rabbit cannot land. The rabbit wants to reach position 'n' from position 0 with the minimum number of jumps. The rabbit always jumps forward and cannot overshoot 'n'.
</details>

<details>
<summary>Ladder</summary>
A boy climbs a ladder. He can take either one step or two steps at a time. We want to determine the number of different ways he can reach the top of the ladder. Since the number of ways can be very large, we only need to return the result modulo 2^p.
</details>

<details>
<summary>Meeting</summary>
At the second congress of the Bajtocki Informatics Society, the participants are seated around a circular table.
One participant posed the question: how many ways can they greet each other without standing up?
A greeting consists of each participant shaking hands with at most one of their neighbors.
The number of ways can be large, so they are only interested in the last digit of the result.
</details>


### Recursion 

<details>
<summary>Add Two Numbers</summary>
Add two numbers, but they are a reversed list

Example
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
https://leetcode.com/problems/add-two-numbers/
</details>

<details>
<summary>Bucket Fill</summary>
Bucket Fill tool implementation

For an image (n x m array of color as a signle number), apply bucket fill to a pixel with a certain color and print out result image.
</details>

<details>
<summary>Factorization</summary>
For a number, print out factorization. Use recursion.
</details>

<details>
<summary>Ineffective Fibonacci</summary>
Use recursion to compute n-th Fibonacci number. DO NOT optimize. Make it real bad, but recursive.
</details>

<details>
<summary>Fibonacci Memorization</summary>
Fix Ineffective Fibonacci. Still, use recursion but make it smarter.
</details>

<details>
<summary>Find Peak</summary>
Find any array peak (that is, for an i-th value in a list, both values on right and left are smaller).
</details>

<details>
<summary>Power Slow</summary>
For values x and n, compute x to the power of n. Do not worry about optimization. Just make it recursive.
</details>

<details>
<summary>Power Fast</summary>
For values x and n, compute x to the power of n. Try to optimize. 
</details>

<details>
<summary>Hanoi</summary>
Classic Tower of Hanoi problem.
</details>

### Binary Search

<details>
<summary>Distance</summary>
For a set of queries (a, b) on a sorted array (arr), find largest distance between value a and b in the array.
</details>

<details>
<summary>Split Array</summary>
Find smallest amount, such that a list can be divided into k segments where each segment's sum does not exceed this amount.
</details>

<details>
<summary>Nails</summary>
Find minimum number of nails that need to be nailed in order for all plates to be nailed. You are given plate start and end point, and nail locations in order of nailing.
</details>

<details>
<summary>Radius</summary>
</details>

### Two Pointer Technique

<details>
<summary>Treats</summary>
A girl placed n treats in a row. Each treat is of a certain type. 
The girl can now choose a certain number (from 1 to n) of consecutive treats and then eat them all. 
The only condition is that no two treats can be of the same type. 
Help the girl and find the number of ways in which she can choose such consecutive treats.
</details>


<details>
<summary>Cutout</summary>
Jasio found a very old roll of paper in the attic on which his great-grandfather had written a sequence of integers.
For a game he recently invented, he needs a segment of the paper where the sum of all numbers is exactly `s`.
He will throw away the unnecessary parts.
Additionally, Jasio wants this segment to be as long as possible.
</details>


<details>
<summary>Temperature</summary>
We are given temperature readings from two thermometers: one on the north wall and one on the south wall.
- The north wall thermometer *never shows higher* than the actual temperature.
- The south wall thermometer *never shows lower* than the actual temperature.
This means the true temperature on day i lies within the interval [north[i], south[i]].

Return the length of the longest contiguous time interval (subarray) during which it was possible that the actual temperatures were non-decreasing.
</details>

### Greedy

<details>
<summary>Kayakers</summary>
We have `n` kayakers, each with a weight such that 1 <= w_0 <= w_1 <= ... <= w_(n-1) <= 10^9.
We want to assign them to the minimum number of two-person kayaks with a weight capacity of `k`. 
Each kayak can hold up to two people as long as their combined weight does not exceed `k`. 
It is guaranteed that each individual weighs less than or equal to `k`, so everyone can go alone if necessary.
</details>

<details>
<summary>Ropes</summary>

A boy received n strings from his grandfather, laid out in a straight line, one after another.
He noticed that he can freely tie any two adjacent strings together to form one longer string.
The resulting string has a length equal to the sum of the two original strings, and it can again be tied with the next adjacent string.

The boy wants to end up with as many strings as possible, with the constraint that each resulting string must be at least as long as his height h.
</details>

<details>
<summary>Sticks</summary>
You are given an N (1 <= N <= 50), number of sticks. 
Each stick has a length a_i (1 <= a_i <= 10^9). 
Each stick can be split in half. The resulting sticks have to be integers.
So, we define the lenghts of resulting sticks as floor(a_i / 2) and a_i - floor(a_i / 2).
Whenever you split a stick, you save one and throw out the other.
For a sequence of sticks, reply with minimum number of splitting operations required to make all sticks same length.
For example, sticks [5, 6, 5, 6] can all become of length 3 in total of 4 operations.
</details>

<details>
<summary>Boxes</summary>
You are given a sequence of n distinct integers from 1 to n, stored inside n boxes. 
There is one additional empty box labeled n+1.
At any time, you are allowed to swap the content of the empty box with any other box.
Your goal is to sort the boxes so that box i contains the integer i for all 1 ≤ i ≤ n. 
Determine some, true number of swap operations needed using the empty box, and print the sequence of positions you used to swap with the empty box (including the final swap that places n+1 back in position n+1).
If the number of operations exceeds 1500, do not output anything.
</details>

<details>
<summary>Make Palindrome</summary>
You are given a t, number of test cases.
For each testcase, you are given a string s.
Find minimum number of 'x' that need to be inserted into s so it becomes a palindrome.
Print -1 if not possible.
</details>

<details>
<summary>Glasses</summary>
A girl lined up a number of glasses and poured the same amount of water into each one.
Then she left the room. During her absence, a boy came in and decided to play a prank
by quickly pouring water between the glasses, making the water levels uneven.

When the girl returned and saw the uneven water distribution, she got upset and ran to her mother.
An investigation could not find the culprit, so now the only thing to do is to redistribute the water
such that each glass ends up with the same amount of water.

Given the current amount of water in each glass, determine whether it's possible to make all glasses
contain the same amount, and if so, compute the minimum number of water transfer operations needed.
A transfer consists of pouring water from one glass to another.
</details>

### Dynamic Programming

<details>
<summary>Frog</summary>
A frog wants to jump from position 0 to position k using fixed jump lengths s0, s1, ..., sn-1.
It can only jump in the forward direction. Your task is to count how many different ways
the frog can reach exactly position k by making any number of jumps (including zero),
using the allowed jump distances.
</details>

<details>
<summary>Board</summary>
A girl received a board with `n` fields, each containing an integer: p0, p1, ..., p(n-1).
A boy came up with a game:

Starting from position 0, you must move a token to position n-1 by rolling a six-sided die.
Each move lets you jump 1 to 6 fields forward.

The goal is to collect the highest possible total by summing the values of all visited fields,
starting from position 0 and ending at position n-1.

Return the maximum sum you can get by playing optimally.
</details>

<details>
<summary>Highway</summary>
In Bajtlandia, there are `n` cities located along a coastline. Each pair of consecutive cities
is connected by a one-way sandy road, and traveling along such a road takes exactly one day.

Additionally, from each city, there might be a one-way highway leading to another city.
Traveling via a highway also takes one day. However, due to the high cost, you are allowed to use
highways at most `k` times during the entire journey.

Michał wants to get from the first city (index 0) to the last city (index n-1) as quickly as possible.

You are given the number of cities `n`, the maximum allowed number of highway uses `k`,
and an array `m` of length `n` where:
- `m[i] == -1` means there is no highway from city i
- `m[i] == j` means there is a highway from city i to city j

Calculate the minimum number of days needed to travel from city 0 to city n-1,
using at most `k` highways.
</details>

<details>
<summary>Pretty Sequence</summary>
A boy is constructing sequences made of integers in the range from 0 to k.
He considers a sequence "nice" if the absolute difference between any two
adjacent elements is at most 1.

We want to find out how many different nice sequences of each given length
can be formed. Two sequences are considered different if they differ at
any position.

Your task is to calculate, for each given sequence length, the number of such
nice sequences, modulo q.
</details>

### Compression

<details>
<summary>Papers</summary>
You are given t, number of testcases.
For each testcase, find the following: 
You are given left bottom corrner coordinates and upper top corner coordinates of three papers (white, black and black).
The papers are placed on a grid as given. Check if after placing black papers, the white one is still visible.
Coordinates have value up to 10^6 and are positive integers.
Print YES or NO.
</details>

### Simulations

<details>
<summary>Snake</summary>
TLDR; simulate snake game given apple locations and snake movements. write how long it will live.

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

</details>

<details>
<summary>2048</summary>
2048 is a fun single-player game played on an N x N board. In this game, the player moves all the blocks on the board in one of four directions — up, down, left, or right. When two blocks with the same value collide during a move, they merge into one block with a value equal to their sum. However, a block can only merge once per move.

In this version of the game:

No new blocks are added after each move (unlike the original 2048 game).
If three identical blocks are lined up in a direction, only the leading pair will merge first (e.g., [2, 2, 2] moving left becomes [4, 2], not [2, 4]).
Your goal is to determine the maximum block value that can be created after performing at most 5 moves.
You are given the initial state of the board. Write a program to find the largest possible block value obtainable in five or fewer moves.
</details>

<details>
<summary>Beads</summary>
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
</details>

## Advanced Algorithms

### Binary Tree

<details>
<summary>Min Path</summary>
For a given binary tree, find a path with minum sum from root to a leaf.
</details>

### DFS

<details>
<summary>All Paths from Source Lead to Destination</summary>
Given graph, source, and destination - check if all paths lead to destination.
https://leetcode.com/problems/all-paths-from-source-lead-to-destination/description/
</details>

<details>
<summary>Tree Distances I</summary>
You are given a tree consisting of n nodes. Your task is to determine for each node the maximum distance to another node.
https://cses.fi/alon/task/1132
</details>

<details>
<summary>Longest Increasing Path In A Matrix</summary>
Find longest path that has increasing value in each consecutive cell. 
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
</details>

<details>
<summary>Loud and rich</summary>
Find longest path that has increasing value in each consecutive cell. 
https://leetcode.com/problems/loud-and-rich/description/
</details>

<details>
<summary>Valid Tree</summary>
Check if a tree is a valid tree.
</details>

### Dijkstra

<details>
<summary>Restricted paths</summary>
There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.

https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/description/
</details>

### Find and Union

<details>
<summary>Evaluate Division</summary>
Given a series of proportions between variables, evaluate proportions between other pairs if possible
https://leetcode.com/problems/evaluate-division/description/
</details>


<details>
<summary>Valid Tree</summary>
Check if a tree is a valid tree.
</details>

### MST

<details>
<summary>Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
</summary>
Find critical edges (MST cannot exist without this edge), and pseudo-critical edges (MST can, but does not have to exist with this edge) for a given graph.
</details>

<details>
<summary>Min Cost to Connect All Points</summary>
Find a MST for a set of nodes represented as points on a 2D grid.
https://leetcode.com/problems/min-cost-to-connect-all-points/description/
</details>

<details>
<summary>Optimize Water Distribution in a Village</summary>
Every house in a village needs water. House can get water from other hourse or by getting a well. Each operation has different cost. Compute cost of getting water to all the houses in a village.
https://leetcode.com/problems/optimize-water-distribution-in-a-village/description/
</details>

### Topological Sort

<details>
<summary>Minimum Height Tree</summary>
Take a Tree and find node to make the height of tree minimum.
https://leetcode.com/problems/minimum-height-trees/description/
</details>

<details>
<summary>Sequence Reconstruction</summary>
Check if a sequence can be uniqely reconstructed from dependencies.
https://leetcode.com/problems/sequence-reconstruction/description/
</details>

### DP on a Tree

<details>
<summary>Maximal Point Path</summary>
For a given tree, crossing each edge costs points. Each node visit adds points. Given amount of points earned by node visit and amount of points lost by traveling through an edge, compute a path that results in heighest point gain. 
</details>

<details>
<summary>Maximum Height of Tree</summary>
Find maximum height of tree when any node could be a root.
</details>

<details>
<summary>Maximum Set of Edges</summary>
 Given a tree consisting of N Nodes and N-1 edges. 
The task is to select the maximum set of edges such that each vertex is part of at most one of the selected edges (no two edges share a common end point) 
i.e., if we select an edge connecting vertex u and v, then we cannot select any other edge connected by vertex u or vertex v.
</details>

<details>
<summary>Sum of Distances In Tree</summary>
Compute for each node a sum of distances to all other nodes.
https://leetcode.com/problems/sum-of-distances-in-tree/description/
</details>

### Hashing

<details>
<summary>Unique Subwords</summary>
For a given word, count all unique subwords inside that word.
Example:
ABAB

Answer:
7 
(A, B, AB, BA, ABA, BAB, ABAB)
</details>

### Text 

<details>
<summary>XX</summary>
Given a string s, find the minimum number of operations required to make the string in a format of X+X.

Allowed operations include:
1. Deleting a letter from s
2. Adding a letter to s
3. Replacing a letter in s

For example, "XYXX" -> requires 1 operation. 
"ABCXYZDEFABCDEF" -> requires 3 operaitons.
</details>



# Implementation

This is a place where I keep my implementation of most popular algorithms.

## Sorting

* Count Sort (python)
* Heap Sort (C++)
* Insert Sort (C++, python)
* Merge Sort (C++, python)
* Quick Sort (C++)
* Selection Sort (python)
* Topological Sort (C++, with and without queue)
* Unique Count (python)

## Graphs

* BFS (C++)
* DFS (C++)
* Dijkstra (C++)
* Bellman-Ford (C++)
* Floyd-Warshall (C++)
* Tree Diameter (C++)
* MST Kruskal (C++)
* MST Prim (C++)

## Other

* prefix sum (python)
* 2D prefix sum (C++, python)
* 2-pointer technique (C++)
* Binary Search (C++, python)
* Binary Tree (C++)
* Binary Heap (C++)
* Find and Union (C++)
* Maximum Subarray Sum (python)
* Maximum 2D Subarray Sum (python)
* Sieve of Eratosthenes (python)
* Factorization with sieve (python)
* Levenshtein Distance (C++, python)

# Testing

Testing is an example on testing your competition solutions - write a generate.cpp code to generate example inputs, write a solution in main.cpp and a brute-force solution in test.cpp. Then use test.sh to find any cases where they give different results.