N = int(input())
satisfied = False

for i in range(2, N) :
    if N % i == 0 :
        satisfied = True
        break

print('C' if satisfied == True else 'N')