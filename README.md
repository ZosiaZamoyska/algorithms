# Algorithms

Algorithm implementations and solutions, mostly for introductory competetive programming. Includes implementations, problems and solutions for some topics, and introduction to testing your solutions.

# Teaching solutions

Keeping implementation of algorithmic problems on different problems by topic.

## Introduction to Algorithms

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


### Dijkstra

<details>
<summary>Restricted paths</summary>
There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.

https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/description/
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

# Testing

Testing is an example on testing your competition solutions - write a generate.cpp code to generate example inputs, write a solution in main.cpp and a brute-force solution in test.cpp. Then use test.sh to find any cases where they give different results.