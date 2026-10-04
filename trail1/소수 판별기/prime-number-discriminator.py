N = int(input())
satisfied = True

for i in range(2, N) :
    if N % i == 0 :
        satisfied = False
        break

print('P' if satisfied == True else 'C')