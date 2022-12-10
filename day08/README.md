👉 ADVENT OF CODE (Day 08) 👈

🔗 Problem Link: https://adventofcode.com/2022/day/8

-: Part 1 :-

Traverse the matrix row-wise and column-wise and keep track of the max value so far. Every time you encounter a new max value, update the max value and mark the corresponding row and column.
Finally find the total number of marked rows and columns.

-: Part 2 :-

Again traverse the entire matrix. For each item in the matrix, count the number of steps you can move up, down, left and right untill you hit a bigger tree or the wall. The score for that tree is the product of the number of steps you can move in each direction. Keep track of the max score so far. The answer is the max score.


Link to my solution: https://github.com/arnabsen1729/aoc-2022/blob/main/day08/solution.py
#adventofcode