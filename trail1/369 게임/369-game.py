N = int(input())

for i in range(1, N + 1) :
    if i % 3 == 0 or ((i // 100 in [3, 6, 9]) or (i % 100 // 10 in [3, 6, 9]) or (i % 10 in [3, 6, 9])) :
        print(0, end = ' ')
    else :
        print(i, end = ' ')