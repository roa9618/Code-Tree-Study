satisfied = True 

for _ in range(5) :
    number = int(input())

    if number % 3 != 0 :
        satisfied = False

print(1 if satisfied == True else 0)