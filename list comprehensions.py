f _name_ == '_main_':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = []
    num = []
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    num = [X,Y,Z]
                    output.append(num)
print(output)
