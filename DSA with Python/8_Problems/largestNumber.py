
def find_largest(numbers):
    largest = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]

    return largest


numbers = [12, 7, 25, 9, 18]

print(find_largest(numbers))
