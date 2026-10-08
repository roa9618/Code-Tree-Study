N = int(input())

for i in range(N * 2) :
    if i % 2 == 0 :
        for j in range(1 + i // 2) :
            print('*', end = ' ')
        print()
    else :
        for j in range(N - (i - 1) // 2) :
            print('*', end = ' ')
        print()