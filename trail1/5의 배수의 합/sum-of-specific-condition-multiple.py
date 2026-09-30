A, B = map(int, input().split())
sum = 0

for i in range(min(A, B), max(A, B) + 1) :
    if i % 5 == 0 :
        sum += i

print(sum)