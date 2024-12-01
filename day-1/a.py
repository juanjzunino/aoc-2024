# Answer: 2066446

with open("day-1/input.txt") as f:
    file = f.readlines()
    list_a = []
    list_b = []
    for line in file:
        components = line.split("   ")
        list_a.append(int(components[0].strip()))
        list_b.append(int(components[1].strip()))
    list_a.sort()
    list_b.sort()

diff = sum(abs(a - b) for a, b in zip(list_a, list_b))
print(diff)
