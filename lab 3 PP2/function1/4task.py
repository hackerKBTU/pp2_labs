def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]


numbers = list(map(int, input("Enter list of numbers separated by spaces: ").split()))
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)
