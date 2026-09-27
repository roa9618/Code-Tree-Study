person1_age, person1_gender = input().split()
person2_age, person2_gender = input().split()

if (int(person1_age) >= 19 and person1_gender == 'M') or (int(person2_age) >= 19 and person2_gender == 'M') :
    print(1)
else :
    print(0)