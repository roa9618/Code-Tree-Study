while True:
    width, height, word = input().split()
    width = int(width)
    height = int(height)

    print(width * height)

    if word == 'C' :
        break