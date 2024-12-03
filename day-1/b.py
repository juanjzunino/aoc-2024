from collections import Counter

with open('day-1/input.txt') as f:
    file = f.readlines()
    list_a = []
    list_b = []
    for line in file:
        components = line.split('   ')
        list_a.append(int(components[0].strip()))
        list_b.append(int(components[1].strip()))
    list_a.sort()
    list_b.sort()

search_keys = [b for b in list_b if b in list_a]
count = Counter(search_keys)
similarity_score = sum(k * v for k, v in count.items())
print(similarity_score)
