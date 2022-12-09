👉 ADVENT OF CODE (Day 07) 👈

🔗 Problem Link: https://adventofcode.com/2022/day/7

Uff, things are getting interesting on the AOC side.

Today we had to parse a file system from a list of outputs of the command `cd` and `ls`. Taking inspiration from my Operation System course we had this semester, I went ahead and implemented a class called `Node`. The important attributes were `size`, and a list of Nodes called `children`. 

In other words, I implemented a tree data structure with the root at `/`. Once that's done, we can simply traverse the tree and find the total size of the tree and all the directories in it.

Once you have the sizes of all the dirs you can solve both Part 1 and Part 2 with that. In Part 1 just find the dirs whose size is less than 1000 and in Part 2 find the dir whose size is just enough to free the required space.

```python
class Node:
    def __init__(self, name: str, isDirectory: bool, size: int = 0) -> None:
        self.name = name
        self.isDirectory = isDirectory
        self.size = size
        self.children = []

        if not self.isDirectory:
            assert self.children == []

    def add_child(self, child: 'Node') -> None:
        ...

    def get_size(self) -> int:
        ...
```

Link to my solution: https://github.com/arnabsen1729/aoc-2022/blob/main/day07/solution.py