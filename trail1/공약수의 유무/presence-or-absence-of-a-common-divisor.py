A, B = map(int, input().split())
satisfied = False

for i in range(A, B + 1) :
    if 1920 % i == 0 and 2880 % i == 0 :
        satisfied = True
        break

print(1 if satisfied == True else 0)