n = int(input())
inp = [[['' for _ in range(3)] for _ in range(3)] for _ in range(n)]

for i in range(n):
    for j in range(3):
        inp[i][j] = input()

for i in range(n):
    flag = 0
    if inp[i][1][1] != '.' and ((inp[i][0][0] == inp[i][1][1] and inp[i][1][1] == inp[i][2][2]) or (inp[i][0][2] == inp[i][1][1] and inp[i][1][1] == inp[i][2][0])):
        print(inp[i][1][1])
        continue
    for j in range(3):
        if inp[i][1][1] != '.' and (inp[i][j][0] == inp[i][j][1] and inp[i][j][1] == inp[i][j][2]):
            print(inp[i][j][1])
            flag = 1
            break
    if flag:
        continue
    for j in range(3):
        if inp[i][1][1] != '.' and (inp[i][0][j] == inp[i][1][j] and inp[i][1][j] == inp[i][2][j]):
            print(inp[i][1][j])
            flag = 1
            break
    if flag:
        continue
    print("DRAW")

