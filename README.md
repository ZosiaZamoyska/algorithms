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
    - [Recursion](#recursion)
  - [Advanced Algorithms](#advanced-algorithms)
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


## Advanced Algorithms

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

# Testing

Testing is an example on testing your competition solutions - write a generate.cpp code to generate example inputs, write a solution in main.cpp and a brute-force solution in test.cpp. Then use test.sh to find any cases where they give different results.