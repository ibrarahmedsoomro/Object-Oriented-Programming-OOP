def average(numbers):
    total = 0

    for num in numbers:
        total += num

    return total / num

marks = [70, 80, 90, 100]

print(average(marks))