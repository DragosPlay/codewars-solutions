def high_and_low(numbers):
    numbers = [int(num) for num in numbers.split()]
    ans = f'{max(numbers)} {min(numbers)}'
    return ans
