sum = 0
cnt = 0

while True :
    age = int(input())

    if not 19 < age < 30 :
        break

    sum += age
    cnt += 1

print(f"{sum / cnt:.2f}")