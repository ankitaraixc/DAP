def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Product of the numbers:", multiply_list(numbers))
