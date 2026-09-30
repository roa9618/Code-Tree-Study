N = int(input())
sum = 0

for i in range(N) :
    num = int(input())

    if num % 2 != 0 and num % 3 == 0 :
        sum += num

print(sum)