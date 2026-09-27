person_1 = input().split()
person_2 = input().split()
person_3 = input().split()

person_1[1] = int(person_1[1])
person_2[1] = int(person_2[1])
person_3[1] = int(person_3[1])

if person_1[0] == 'Y' and person_1[1] >= 37 :
    if person_2[0] == 'Y' and person_2[1] >= 37 :
        print('E')
    elif person_3[0] == 'Y' and person_3[1] >= 37 :
        print('E')
    else :
        print('N')
else :
    if person_2[0] == 'Y' and person_2[1] >= 37 :
        if person_3[0] == 'Y' and person_3[1] >= 37 :
            print('E')
        else :
            print('N') 
    else :
        print('N')