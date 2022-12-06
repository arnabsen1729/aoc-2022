👉 ADVENT OF CODE (Day 05) 👈

🔗 Problem Link: https://adventofcode.com/2022/day/5

The hardest part was trying to parse the input. So, here's how I approached:

1. Split the entire input by double newlines (i.e. '\n\n`). The first part is the input data and then the second part is the test data.
2. Made an assumption that the crate name will always be a single letter. That way I was able to get the initial position of each of the crates.
3. Then I just had to iterate over the instructions and update the position of the crates accordingly.

I built a simple class to abstract the functioning of the crates.

```
class CrateStack:
    def __init__(self, len) -> None:
        self.stack = [[] for _ in range(len)]
        self.len = len

    def insert(self, index, value):
        self.stack[index].append(value)

    def display(self):
        for i in range(self.len):
            print(f'{i+1}: {self.stack[i]}')

    def move(self, count, from_index, to_index): # FOR PART 1
        from_index -= 1
        to_index -= 1
        for _ in range(count):
            self.stack[to_index].append(self.stack[from_index].pop())

    def move_together(self, count, from_index, to_index): # FOR PART 2
        from_index -= 1
        to_index -= 1
        self.stack[to_index].extend(self.stack[from_index][-count:])
        self.stack[from_index] = self.stack[from_index][:-count]
```

Link to my solution: https://github.com/arnabsen1729/aoc-2022/blob/main/day05/solution.py