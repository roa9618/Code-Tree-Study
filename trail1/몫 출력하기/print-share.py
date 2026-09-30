count = 0

while True :
    num = int(input())

    if num % 2 == 0 :
        print(num // 2)
        count += 1
    
    if count >= 3 :
        break