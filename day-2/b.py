def evaluate(numbers: list[int]) -> tuple[bool, int | None]:
    status = True
    last_direction = None

    for i in range(len(numbers) - 1):
        diff = numbers[i] - numbers[i + 1]

        if diff == 0 or abs(diff) > 3:
            status = False
            return (status, i)

        if last_direction is None:
            last_direction = 'DESC' if diff > 0 else 'ASC'
            continue

        if diff > 0 and last_direction == 'ASC':
            status = False
            return (status, i)

        elif diff < 0 and last_direction == 'DESC':
            status = False
            return (status, i)

    return (status, None)


with open('day-2/input.txt') as f:
    lines = f.readlines()

safe = 0

for line in lines:
    numbers = list(map(lambda x: int(x.strip()), line.split(' ')))
    status, idx = evaluate(numbers)

    if not status:
        number_aux = numbers.copy()
        number_aux.pop(idx)
        status, _ = evaluate(number_aux)

    if not status:
        number_aux = numbers.copy()
        number_aux.pop(idx + 1)
        status, _ = evaluate(number_aux)

    if not status:
        number_aux = numbers.copy()
        number_aux.pop(idx - 1)
        status, _ = evaluate(number_aux)

    if status:
        safe += 1

print(safe)
