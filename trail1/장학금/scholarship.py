mid_term, final_term = map(int, input().split())

if mid_term >= 90 :
    if final_term >= 95 :
        print(100000)
    elif final_term >= 90 :
        print(50000)
    else :
        print(0)
else :
    print(0)