def process_numbers(num):
    num = list(filter(lambda x:x%2==0,num))
    num = list(map(lambda x:x**2,num))
    return num

numbers = [5, 2, 8, 3, 10, 7, 4]
result = process_numbers(numbers)

print(sorted(result, reverse=True))