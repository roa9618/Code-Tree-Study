A, B = map(int, input().split())

print(f"{A // B}.", end = '')

num = A % B

for _ in range(20) :
    num *= 10
    val = num // B
    num %= B

    print(val, end = '')