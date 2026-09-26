arr = list(map(int, input().split()))

print(1 if arr[0] == min(arr) else 0, end = " ")
print(1 if arr[0] == arr[1] == arr[2] else 0)