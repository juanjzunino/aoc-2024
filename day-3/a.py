import re

with open('day-3/input.txt') as f:
    data = f.read()

pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
matches: list[str] | None = re.findall(pattern, data)

if matches:
    cleaned_matches = [match.replace('mul(', '').replace(')', '').split(',') for match in matches]
    totals = sum(int(a) * int(b) for a, b in cleaned_matches)
    print(totals)
