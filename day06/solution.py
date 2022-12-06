f = open('test.txt') 
f = open('input.txt')

line = f.readlines()[0]

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

def sol(n = 4):
    s = Freq()
    for i in range(n):
        s.add(line[i])

    if s.get_total() == n:
        return n

    for i in range(n, len(line)):
        s.remove(line[i-n])
        s.add(line[i])
        if s.get_total() == n:
            return i+1
        
    return -1

print("Part 1:", sol())
print("Part 2:", sol(14))

f.close()