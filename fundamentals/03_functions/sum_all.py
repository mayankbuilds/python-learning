def sum_all(*args):
    total = 0
    for num in args:
        total = total+num
    return total

print(sum_all(30, 40, 50 ,90))