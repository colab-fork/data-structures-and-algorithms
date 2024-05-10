lis = ['s', 'h','a', 's']
while True:
    c = input().split()
    command = c[0]
    if command == 'append':
        lis.append(c[1])
    elif command == 'insert':
        index = int(c[1])
        value = int(c[2])
        lis.insert(index, value)
    elif command == 'print':
        print(lis)
    elif command == 'sort':
        sorted(lis)
    elif command == 'pop':
        lis.pop(-1)
    elif command == 'reverse':
        lis.reverse()
    elif command == 'remove':
        value = c[1]
        for x in lis:
            if x == value:
                lis.remove(x)
                break
    else:
        print("t")