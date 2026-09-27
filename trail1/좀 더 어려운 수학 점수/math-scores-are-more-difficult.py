A_Math, A_English = map(int, input().split())
B_Math, B_English = map(int, input().split())

if A_Math > B_Math :
    print('A')
elif A_Math < B_Math :
    print('B')
else :
    if A_English > B_English :
        print('A')
    else :
        print('B')