f = open('input.txt', 'r')
lines = [l.strip() for l in f.readlines()]
f.close()

calories = []
colorie = 0
for line in lines:
    if line == '':
        calories.append(colorie)
        colorie = 0
    else:
        colorie += int(line)

calories.append(colorie)

sorted_calories = sorted(calories, reverse=True)
print(sum(sorted_calories[0:3]))