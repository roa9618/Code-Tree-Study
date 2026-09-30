sum = 0
cnt = 0

for _ in range(10) :
    num = int(input())

    if 0 <= num <= 200 :
        sum += num
        cnt += 1

print(f"{sum} {sum / cnt:.1f}")