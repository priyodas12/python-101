def get_factorial_result(n):
    if n<1:
        return 1
    else:
        return n*get_factorial_result(n-1)

print(get_factorial_result(14))