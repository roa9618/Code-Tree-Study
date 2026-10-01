N = int(input())
count = 0

while True :
    if N == 1 :
        break
    elif N % 2 == 0 :
        N //= 2
    else :
        N = (N * 3) + 1
    
    count += 1

print(count)