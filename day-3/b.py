import re


def multiply(match: str) -> int:
    a, b = re.sub(r'(mul\(|\))', '', match).split(',')
    return int(a) * int(b)


with open('day-3/input.txt') as f:
    data = f.read()

pattern = re.compile(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))')
matches: list[str] | None = re.findall(pattern, data)

if matches:
    enabled = True
    totals = 0
    for match in matches:
        if 'mul' in match and enabled:
            totals += multiply(match)
        elif 'mul' in match and not enabled:
            continue
        elif 'do()' in match:
            enabled = True
        elif "don't()" in match:
            enabled = False
        else:
            raise Exception('Unexpected match')
    print(totals)
