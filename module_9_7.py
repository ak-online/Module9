def is_prime(func):
    def wrapper(*args):
        orig_res = func(*args)
        for i in range(2, (orig_res // 2) + 1):
            if orig_res % i == 0:
                print("Составное")
            else:
                print("Простое")
            return orig_res

    return wrapper


@is_prime
def sum_three(*args):
    total = 0
    for i in args:
        total += i
    return total


result = sum_three(2, 3, 6)
print(result)

