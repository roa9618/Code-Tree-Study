a, b, c = map(int, input().split())
satisfied = True

for i in range(a, b + 1) :
    if i % c == 0 :
        satisfied = False
        break

print("YES" if satisfied == True else "NO")