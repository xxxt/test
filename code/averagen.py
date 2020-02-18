count = 0
sum = 0
print("Please Input numbers:")
N = 10
while count < N:
    number = float(input())
    sum += number
    count += 1
avg = sum / count
print(avg)
