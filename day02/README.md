-: ADVENT OF CODE (Day 02) :-

Problem Link: https://adventofcode.com/2022/day/2

To simplify the computation, I have assigned integer values to every move:

- Rock is 0
- Paper is 1
- Scissors is 2

If player1 makes move1 and player2 makes move2, then the winner is decided by the difference of the two moves. The possible values of difference are: -2, -1, 0, 1, 2. The winner is decided by the following rules:

- If the difference is 1 or 2, then player1 wins.
- If the difference is -1 or -2, then player2 wins.
- If the difference is 0, then it is a draw.

For part2, we just have to extend this logic, is move1 is the move by first player and the outcomes are:

- DRAW then move2 = move1
- WIN then move2 = (move1 + 1) % 3
- LOSE then move2 = (move1 - 1) % 3

Why % 3? Because we have 3 possible moves, so we need to wrap around the values.

Link to my solution: https://github.com/arnabsen1729/aoc-2022/blob/main/day02/solution.py