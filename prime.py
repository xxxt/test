for i in range(0,101):
    is_prime = True
    for j in range(2,i-1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end='  ')