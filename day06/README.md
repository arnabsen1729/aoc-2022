👉 ADVENT OF CODE (Day 06) 👈

🔗 Problem Link: https://adventofcode.com/2022/day/6

This question comes under the category of sliding window problem. For the first part the window size is 4. And you have the find number of unique characters in the window. If that number is equal to 4, then you have found the position.

To implement the sliding window, you can use a set/map/array. Once you shift the window right by one, you have to add the new character and remove the old character. Since we need to find the number of unique characters we can maintain a total_count. If the removed character count in the map becomes zero that means that character is no longer present in the window. So we have to decrement the total_count. And if the added character count in the map becomes 1 that means that character is newly added to the window. So we have to increment the total_count.

Link to my solution: https://github.com/arnabsen1729/aoc-2022/blob/main/day06/solution.py

```python
class Freq:
    def __init__(self):
        self.freq = {}
        self.total = 0
    
    def add(self, c):
        if c in self.freq:
            self.freq[c] += 1
        else:
            self.freq[c] = 1
            self.total += 1
    
    def remove(self, c):
        if c in self.freq:
            self.freq[c] -= 1
            if self.freq[c] == 0:
                del self.freq[c]
                self.total -= 1

    def get_total(self):
        return self.total
```