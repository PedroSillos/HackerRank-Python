if __name__ == '__main__':
    n = int(input())
    
    l = list()
    
    for i in range(n):
        command, *values = input().split()
        
        values = list(map(int,values))

        if command == 'insert':
            l.insert(values[0], values[1])
        elif command == 'print':
            print(l)
        elif command == 'remove':
            l.remove(values[0])
        elif command == 'append':
            l.append(values[0])
        elif command == 'sort':
            l = sorted(l)
        elif command == 'pop':
            l.pop(-1)
        elif command == 'reverse':
            l.reverse()