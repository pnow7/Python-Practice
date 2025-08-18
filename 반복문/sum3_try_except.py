import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())

        if A == 0 and B == 0:
            break

        print(A+B)
        
    except ValueError:
        break


result = []

while True:
    try:
        C, D = map(int, sys.stdin.readline().split())

        if C == 0 and D == 0:
            break
        
        result.append((C,D))

    except ValueError:
        break
    
for C, D in result:
    print(C+D)
    


