def evaluate(numbers: list[int]) -> bool:
    status = True
    last_direction = None

    for i in range(len(numbers) - 1):
        diff = numbers[i] - numbers[i + 1]

        if diff == 0 or abs(diff) > 3:
            status = False
            return status

        if last_direction is None:
            last_direction = 'DESC' if diff > 0 else 'ASC'
            continue

        if diff > 0 and last_direction == 'ASC':
            status = False
            return status

        elif diff < 0 and last_direction == 'DESC':
            status = False
            return status

    return status


with open('day-2/input.txt') as f:
    lines = f.readlines()

safe = 0

for line in lines:
    numbers = list(map(lambda x: int(x.strip()), line.split(' ')))
    status = evaluate(numbers)

    if not status:
        for i in range(len(numbers)):
            number_aux = numbers.copy()
            number_aux.pop(i)
            status = evaluate(number_aux)
            if status:
                break

    if status:
        safe += 1

print(safe)
