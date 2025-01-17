# Table of Contents
- [Teaching solutions](#teaching-solutions)
  - [Introduction to Algorithms](#introduction-to-algorithms)
    - [Element Occurance](#element-occurance)
    - [Recursion](#recursion)
  - [Advanced Algorithms](#advanced-algorithms)
    - [DFS](#dfs)
    - [Dijkstra](#dijkstra)
    - [Find and Union](#find-and-union)
    - [MST](#mst)
    - [Topological Sort](#topological-sort)
    - [DP on a Tree](#dp-on-a-tree)
- [Implementation](#implementation)
  - [Sorting](#sorting)
  - [Graphs](#graphs)
  - [Other](#other)
- [Testing](#testing)

# Teaching solutions

Keeping implementation of algorithmic problems on different problems by topic.

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
<summary>Tape</summart>
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
* Merge Sort (c++)
* Quick Sort (c++)
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
* 2D prefix sum (C++)
* 2-pointer technique (C++)
* Binary Search (C++, python)
* Binary Tree (C++)
* Binary Heap (C++)
* Find and Union (C++)

# Testing

Testing is an example on testing your competition solutions - write a generate.cpp code to generate example inputs, write a solution in main.cpp and a brute-force solution in test.cpp. Then use test.sh to find any cases where they give different results.